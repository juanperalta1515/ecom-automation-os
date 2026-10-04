"""
Knowledge Base & Persistence Layer
Stores operator rules (Mauro Stendel, media buyers) and tracks product validation & learning logs in SQLite.
"""

import json
import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Any, Optional

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "ecom_data.db")
RULES_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "rules.json")


class KnowledgeBase:
    def __init__(self, db_path: str = DB_FILE, rules_path: str = RULES_FILE):
        self.db_path = db_path
        self.rules_path = rules_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()
        self._seed_rules_if_empty()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        """Initializes database tables if they do not exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Products evaluated and tested table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tested_products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    product_type TEXT NOT NULL, -- 'Viral/Trend' or 'Evergreen'
                    cost_unit REAL NOT NULL,
                    target_price REAL NOT NULL,
                    multiplier REAL NOT NULL,
                    total_score INTEGER NOT NULL,
                    verdict TEXT NOT NULL,
                    status TEXT DEFAULT 'Evaluado', -- 'Evaluado', 'En Testeo', 'Escalado DDP', 'Descartado'
                    notes TEXT,
                    lessons_learned TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Operational Rules table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS operational_rules (
                    id TEXT PRIMARY KEY,
                    author TEXT NOT NULL,
                    category TEXT NOT NULL,
                    title TEXT NOT NULL,
                    rule TEXT NOT NULL,
                    actionable_tip TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def _seed_rules_if_empty(self):
        """Loads default rules from data/rules.json if rules table is empty."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) as cnt FROM operational_rules")
                count = cursor.fetchone()["cnt"]
                if count == 0 and os.path.exists(self.rules_path):
                    with open(self.rules_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for r in data.get("creator_rules", []):
                            cursor.execute("""
                                INSERT OR REPLACE INTO operational_rules (id, author, category, title, rule, actionable_tip)
                                VALUES (?, ?, ?, ?, ?, ?)
                            """, (r["id"], r["author"], r["category"], r["title"], r["rule"], r["actionable_tip"]))
                    conn.commit()
        except Exception as e:
            print(f"Warning: Could not seed rules: {e}")

    # --- Product History Methods ---
    def save_product_evaluation(self, data: Dict[str, Any]) -> int:
        """Saves a product evaluation to the database."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tested_products 
                (product_name, category, product_type, cost_unit, target_price, multiplier, total_score, verdict, status, notes, lessons_learned)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("product_name", "Sin Nombre"),
                data.get("category", "General"),
                data.get("product_type", "Viral/Trend"),
                float(data.get("cost_unit", 0.0)),
                float(data.get("target_price", 0.0)),
                float(data.get("multiplier", 0.0)),
                int(data.get("total_score", 0)),
                data.get("verdict", "Descartado"),
                data.get("status", "Evaluado"),
                data.get("notes", ""),
                data.get("lessons_learned", "")
            ))
            conn.commit()
            return cursor.lastrowid

    def get_all_products(self) -> List[Dict[str, Any]]:
        """Retrieves all saved products sorted by newest first."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tested_products ORDER BY created_at DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def update_product_status(self, product_id: int, status: str, lessons_learned: Optional[str] = None):
        """Updates the status and lessons learned for a tested product."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            if lessons_learned is not None:
                cursor.execute("""
                    UPDATE tested_products 
                    SET status = ?, lessons_learned = ?
                    WHERE id = ?
                """, (status, lessons_learned, product_id))
            else:
                cursor.execute("""
                    UPDATE tested_products 
                    SET status = ?
                    WHERE id = ?
                """, (status, product_id))
            conn.commit()

    def delete_product(self, product_id: int):
        """Deletes a product from history."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tested_products WHERE id = ?", (product_id,))
            conn.commit()

    # --- Rules Methods ---
    def get_all_rules(self) -> List[Dict[str, Any]]:
        """Retrieves all operating rules."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM operational_rules ORDER BY category, title")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def add_custom_rule(self, author: str, category: str, title: str, rule: str, actionable_tip: str) -> str:
        """Adds a custom rule to the knowledge base."""
        rule_id = f"rule_custom_{int(datetime.now().timestamp())}"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO operational_rules (id, author, category, title, rule, actionable_tip)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (rule_id, author, category, title, rule, actionable_tip))
            conn.commit()
        return rule_id
