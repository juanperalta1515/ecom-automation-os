"""
Knowledge Base & Persistence Layer
Stores operator rules and tracks product validation & learning logs.
Supports dual-mode: SQLite (desktop/server) and JSON-file fallback (WebAssembly/Pyodide on Netlify).
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

try:
    import sqlite3
    HAS_SQLITE = True
except ImportError:
    sqlite3 = None
    HAS_SQLITE = False

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "ecom_data.db")
JSON_DB_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "ecom_db.json")
RULES_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "rules.json")


class KnowledgeBase:
    def __init__(self, db_path: str = DB_FILE, json_path: str = JSON_DB_FILE, rules_path: str = RULES_FILE):
        self.db_path = db_path
        self.json_path = json_path
        self.rules_path = rules_path
        self.use_sqlite = HAS_SQLITE

        os.makedirs(os.path.dirname(self.json_path), exist_ok=True)
        self._init_db()
        self._seed_rules_if_empty()

    def _get_connection(self):
        if not self.use_sqlite:
            return None
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _read_json_db(self) -> Dict[str, Any]:
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "tested_products": [],
            "operational_rules": [],
            "search_learning_log": [],
        }

    def _write_json_db(self, data: Dict[str, Any]):
        try:
            with open(self.json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save JSON DB: {e}")

    def _init_db(self):
        """Initializes database tables or JSON structure."""
        if self.use_sqlite:
            try:
                with self._get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tested_products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_name TEXT NOT NULL,
                            category TEXT NOT NULL,
                            product_type TEXT NOT NULL,
                            cost_unit REAL NOT NULL,
                            target_price REAL NOT NULL,
                            multiplier REAL NOT NULL,
                            total_score INTEGER NOT NULL,
                            verdict TEXT NOT NULL,
                            status TEXT DEFAULT 'Evaluado',
                            notes TEXT,
                            lessons_learned TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
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
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS search_learning_log (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            search_query TEXT,
                            category_filter TEXT,
                            selected_product_name TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    conn.commit()
            except Exception:
                self.use_sqlite = False
                self._init_db()
        else:
            db_data = self._read_json_db()
            self._write_json_db(db_data)

    def _seed_rules_if_empty(self):
        """Loads default rules from data/rules.json if empty."""
        try:
            if self.use_sqlite:
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
            else:
                db_data = self._read_json_db()
                if not db_data.get("operational_rules") and os.path.exists(self.rules_path):
                    with open(self.rules_path, "r", encoding="utf-8") as f:
                        rules_content = json.load(f)
                        db_data["operational_rules"] = rules_content.get("creator_rules", [])
                    self._write_json_db(db_data)
        except Exception as e:
            print(f"Warning: Could not seed rules: {e}")

    # --- Product History Methods ---
    def save_product_evaluation(self, data: Dict[str, Any]) -> int:
        """Saves a product evaluation to the database."""
        if self.use_sqlite:
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
        else:
            db_data = self._read_json_db()
            prods = db_data.get("tested_products", [])
            new_id = len(prods) + 1
            record = {
                "id": new_id,
                "product_name": data.get("product_name", "Sin Nombre"),
                "category": data.get("category", "General"),
                "product_type": data.get("product_type", "Viral/Trend"),
                "cost_unit": float(data.get("cost_unit", 0.0)),
                "target_price": float(data.get("target_price", 0.0)),
                "multiplier": float(data.get("multiplier", 0.0)),
                "total_score": int(data.get("total_score", 0)),
                "verdict": data.get("verdict", "Descartado"),
                "status": data.get("status", "Evaluado"),
                "notes": data.get("notes", ""),
                "lessons_learned": data.get("lessons_learned", ""),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            prods.insert(0, record)
            db_data["tested_products"] = prods
            self._write_json_db(db_data)
            return new_id

    def get_all_products(self) -> List[Dict[str, Any]]:
        """Retrieves all saved products sorted by newest first."""
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tested_products ORDER BY created_at DESC")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        else:
            db_data = self._read_json_db()
            return db_data.get("tested_products", [])

    def update_product_status(self, product_id: int, status: str, lessons_learned: Optional[str] = None):
        """Updates the status and lessons learned for a tested product."""
        if self.use_sqlite:
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
        else:
            db_data = self._read_json_db()
            for p in db_data.get("tested_products", []):
                if p["id"] == product_id:
                    p["status"] = status
                    if lessons_learned is not None:
                        p["lessons_learned"] = lessons_learned
                    break
            self._write_json_db(db_data)

    def delete_product(self, product_id: int):
        """Deletes a product from history."""
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM tested_products WHERE id = ?", (product_id,))
                conn.commit()
        else:
            db_data = self._read_json_db()
            db_data["tested_products"] = [p for p in db_data.get("tested_products", []) if p["id"] != product_id]
            self._write_json_db(db_data)

    # --- Rules Methods ---
    def get_all_rules(self) -> List[Dict[str, Any]]:
        """Retrieves all operating rules."""
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM operational_rules ORDER BY category, title")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        else:
            db_data = self._read_json_db()
            return db_data.get("operational_rules", [])

    def add_custom_rule(self, author: str, category: str, title: str, rule: str, actionable_tip: str) -> str:
        """Adds a custom rule to the knowledge base."""
        rule_id = f"rule_custom_{int(datetime.now().timestamp())}"
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO operational_rules (id, author, category, title, rule, actionable_tip)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (rule_id, author, category, title, rule, actionable_tip))
                conn.commit()
        else:
            db_data = self._read_json_db()
            rules = db_data.get("operational_rules", [])
            rules.append({
                "id": rule_id,
                "author": author,
                "category": category,
                "title": title,
                "rule": rule,
                "actionable_tip": actionable_tip,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            db_data["operational_rules"] = rules
            self._write_json_db(db_data)
        return rule_id

    # --- Search & Learning Methods ---
    def log_search(self, search_query: str, category_filter: str, selected_product_name: Optional[str] = None):
        """Logs user search query to track interests and train system patterns."""
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO search_learning_log (search_query, category_filter, selected_product_name)
                    VALUES (?, ?, ?)
                """, (search_query.strip(), category_filter, selected_product_name))
                conn.commit()
        else:
            db_data = self._read_json_db()
            logs = db_data.get("search_learning_log", [])
            logs.insert(0, {
                "id": len(logs) + 1,
                "search_query": search_query.strip(),
                "category_filter": category_filter,
                "selected_product_name": selected_product_name,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            db_data["search_learning_log"] = logs[:100]  # keep top 100
            self._write_json_db(db_data)

    def get_search_learning_insights(self) -> Dict[str, Any]:
        """Analyzes historical search logs to surface trending niches and search frequency."""
        if self.use_sqlite:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) as total_searches FROM search_learning_log")
                total_searches = cursor.fetchone()["total_searches"]

                cursor.execute("""
                    SELECT category_filter, COUNT(*) as cnt 
                    FROM search_learning_log 
                    WHERE category_filter != 'Todas las Categorías'
                    GROUP BY category_filter 
                    ORDER BY cnt DESC LIMIT 5
                """)
                top_categories = [dict(row) for row in cursor.fetchall()]

                cursor.execute("""
                    SELECT selected_product_name, COUNT(*) as cnt 
                    FROM search_learning_log 
                    WHERE selected_product_name IS NOT NULL AND selected_product_name != ''
                    GROUP BY selected_product_name 
                    ORDER BY cnt DESC LIMIT 5
                """)
                top_analyzed_products = [dict(row) for row in cursor.fetchall()]

                cursor.execute("SELECT * FROM search_learning_log ORDER BY created_at DESC LIMIT 10")
                recent_logs = [dict(row) for row in cursor.fetchall()]

                return {
                    "total_searches": total_searches,
                    "top_categories": top_categories,
                    "top_analyzed_products": top_analyzed_products,
                    "recent_logs": recent_logs,
                }
        else:
            db_data = self._read_json_db()
            logs = db_data.get("search_learning_log", [])
            total_searches = len(logs)

            cat_counts: Dict[str, int] = {}
            prod_counts: Dict[str, int] = {}
            for entry in logs:
                cat = entry.get("category_filter")
                if cat and cat != "Todas las Categorías":
                    cat_counts[cat] = cat_counts.get(cat, 0) + 1
                prod = entry.get("selected_product_name")
                if prod:
                    prod_counts[prod] = prod_counts.get(prod, 0) + 1

            top_categories = [{"category_filter": k, "cnt": v} for k, v in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)[:5]]
            top_analyzed_products = [{"selected_product_name": k, "cnt": v} for k, v in sorted(prod_counts.items(), key=lambda x: x[1], reverse=True)[:5]]

            return {
                "total_searches": total_searches,
                "top_categories": top_categories,
                "top_analyzed_products": top_analyzed_products,
                "recent_logs": logs[:10],
            }
