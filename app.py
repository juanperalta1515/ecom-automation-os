"""
E-Commerce Automation OS (ecom-automation-os)
Executive Interactive Dashboard for Product Discovery, Fast Validation, Store Setup, 3:2:2 Creatives, Media Buying & Sourcing Scale.
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime
from modules.product_catalog import ProductCatalog, CURATED_PRODUCTS
from modules.product_radar import ProductRadar
from modules.validation_blueprint import ValidationBlueprint
from modules.ai_creative_factory import AICreativeFactory
from modules.ads_analytics import AdsAnalytics
from modules.sourcing_hub import SourcingHub
from modules.knowledge_base import KnowledgeBase

# --- Page Configuration ---
st.set_page_config(
    page_title="E-Com Automation OS | Scale & Validation Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom Modern Dark Aesthetics CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        padding: 22px 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    
    .badge-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-right: 8px;
    }
    .badge-trend { background: rgba(244, 63, 94, 0.2); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); }
    .badge-evergreen { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .badge-pro { background: rgba(99, 102, 241, 0.2); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.4); }

    .product-card {
        background: rgba(30, 41, 59, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        transition: all 0.2s ease;
    }
    .product-card:hover {
        border-color: rgba(99, 102, 241, 0.5);
        box-shadow: 0 8px 20px -4px rgba(99, 102, 241, 0.2);
    }
    
    .verdict-box-success {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.85) 0%, rgba(6, 95, 70, 0.5) 100%);
        border: 1px solid #10b981;
        border-radius: 14px;
        padding: 20px 24px;
        color: #ecfdf5;
    }
    .verdict-box-warning {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.85) 0%, rgba(146, 64, 14, 0.5) 100%);
        border: 1px solid #f59e0b;
        border-radius: 14px;
        padding: 20px 24px;
        color: #fffbeb;
    }
    .verdict-box-error {
        background: linear-gradient(135deg, rgba(136, 19, 55, 0.85) 0%, rgba(159, 18, 57, 0.5) 100%);
        border: 1px solid #f43f5e;
        border-radius: 14px;
        padding: 20px 24px;
        color: #fff1f2;
    }
    
    .pipeline-step-card {
        background: #1e293b;
        border-left: 5px solid #6366f1;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 14px;
    }
    
    .script-hook-card {
        background: #1e293b;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }

    div.stButton > button:first-child {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialize Knowledge Base & Session State ---
kb = KnowledgeBase()

if "selected_product" not in st.session_state:
    st.session_state.selected_product = CURATED_PRODUCTS[0]

if "current_product_eval" not in st.session_state:
    p0 = st.session_state.selected_product
    st.session_state.current_product_eval = ProductRadar.evaluate_product(
        product_name=p0["name"],
        category=p0["category"],
        product_type=p0["product_type"],
        cost_unit=p0["cost_unit"],
        target_price=p0["target_price"],
        wow_factor_score=p0.get("wow_factor", 8),
        pain_passion_score=p0.get("pain_passion", 9),
        offline_scarcity_score=p0.get("offline_scarcity", 8),
        has_size_variants=p0.get("has_size_variants", False),
        is_fragile=p0.get("is_fragile", False),
        is_heavy_or_bulky=p0.get("is_heavy", False),
        is_electric_or_battery_risk=p0.get("is_battery", False),
    )

STEPS = [
    "🔍 1. Buscador & Descubrimiento",
    "🎯 2. Radar de 5 Pilares",
    "🛍️ 3. Creación de Tienda & Dropshipping",
    "🎨 4. Fábrica de Creativos (3:2:2)",
    "📊 5. Control de Pauta (Kill/Scale)",
    "🚢 6. Importación DDP & Fábricas",
    "🧠 7. Memoria & Aprendizaje",
]

if "active_step" not in st.session_state:
    st.session_state.active_step = STEPS[0]

# --- Sidebar Header & Navigation Info ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1556742049-0a67e557b6f6?w=400&auto=format&fit=crop&q=80", use_container_width=True)
    st.markdown("## ⚡ **E-Com Automation OS**")
    st.caption("Pipeline paso a paso: Búsqueda ➔ Validación ➔ Tienda DS ➔ Creativos ➔ Pauta ➔ Sourcing DDP.")
    
    st.markdown("---")
    st.markdown("### 🧭 **Navegación del Pipeline**")
    selected_nav = st.radio(
        "Ir al Paso:",
        STEPS,
        index=STEPS.index(st.session_state.active_step) if st.session_state.active_step in STEPS else 0,
        key="sidebar_step_selector"
    )
    if selected_nav != st.session_state.active_step:
        st.session_state.active_step = selected_nav
        st.rerun()

    st.markdown("---")
    # Quick DB statistics
    products_history = kb.get_all_products()
    approved_count = sum(1 for p in products_history if "APROBADO" in p.get("verdict", ""))
    learning_stats = kb.get_search_learning_insights()
    
    st.markdown("### 📊 **Métricas del Workspace**")
    col_sb1, col_sb2 = st.columns(2)
    col_sb1.metric("Evaluados", len(products_history))
    col_sb2.metric("Aprobados", approved_count)
    st.caption(f"🧠 Búsquedas registradas: **{learning_stats['total_searches']}**")

    st.markdown("---")
    st.caption("v1.3.0 • Production Ready (Pipeline Wizard)")

# --- Top Header ---
active_prod_name = st.session_state.selected_product.get("name", "Ninguno seleccionado")
st.markdown(f"""
<div class="main-header">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
        <div>
            <span class="badge-tag badge-trend">🔥 Trend-Driven</span>
            <span class="badge-tag badge-evergreen">🌲 Evergreen Engine</span>
            <span class="badge-tag badge-pro">⚡ DTC Scale Framework</span>
            <h1 style="color: #ffffff; margin: 10px 0 6px 0; font-size: 2.0rem; font-weight: 800;">
                E-Commerce Automation OS
            </h1>
            <p style="color: #94a3b8; margin: 0; font-size: 0.95rem;">
                Producto Activo en Pipeline: <strong style="color: #38bdf8;">{active_prod_name}</strong> | Fase Actual: <strong style="color: #a5b4fc;">{st.session_state.active_step}</strong>
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

current_step = st.session_state.active_step

# ==============================================================================
# PASO 1: BUSCADOR & DESCUBRIMIENTO DE OPORTUNIDADES
# ==============================================================================
if current_step == STEPS[0]:
    st.markdown("### 🔍 **Paso 1: Buscador & Descubrimiento de Oportunidades por Categoría**")
    st.caption("Explora productos pre-investigados, descubre oportunidades en base a tus búsquedas y carga cualquiera al Radar de Validación con 1 clic.")

    c_f1, c_f2, c_f3 = st.columns([1.5, 1, 1])
    with c_f1:
        cat_filter = st.selectbox("Filtrar por Categoría", ProductCatalog.get_all_categories(), key="cat_filter_select")
    with c_f2:
        type_filter = st.selectbox("Naturaleza del Producto", ["Todos", "Evergreen", "Viral/Trend"], key="type_filter_select")
    with c_f3:
        query_filter = st.text_input("Buscar por palabra clave", placeholder="ej: lumbar, aspiradora, facial...", key="query_filter_text")

    filtered_prods = ProductCatalog.search_products(
        category=cat_filter,
        product_type=type_filter,
        search_query=query_filter,
    )

    st.markdown(f"**Se encontraron `{len(filtered_prods)}` productos candidatos:**")

    for p in filtered_prods:
        mult = round(p["target_price"] / p["cost_unit"], 2)
        badge_cls = "badge-evergreen" if p["product_type"] == "Evergreen" else "badge-trend"
        
        with st.container():
            st.markdown(f"""
            <div class="product-card">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                    <div>
                        <span class="badge-tag {badge_cls}">{p['product_type']}</span>
                        <span class="badge-tag badge-pro">{p['category']}</span>
                        <h3 style="color:#ffffff; margin:8px 0 4px 0; font-size:1.2rem;">{p['name']}</h3>
                        <p style="color:#94a3b8; font-size:0.92rem; margin:0 0 10px 0;">{p['description']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_det1, c_det2, c_det3, c_det4, c_det5 = st.columns([1, 1, 1, 1.8, 1.3])
            c_det1.metric("Costo Fábrica", f"${p['cost_unit']:.2f}")
            c_det2.metric("PVP Sugerido", f"${p['target_price']:.2f}")
            c_det3.metric("Multiplicador", f"{mult}X")
            with c_det4:
                st.caption(f"**🚚 Dropshipping:** {p['dropship_platform']}")
                st.caption(f"**🇨🇳 Búsqueda Fábrica:** `{p['china_keywords']}`")
            with c_det5:
                # 1-Click Action to load, evaluate, log search learning, and jump directly to Step 2
                if st.button("🚀 Analizar en Radar & Validar", key=f"btn_analyze_{p['id']}", use_container_width=True, type="primary"):
                    st.session_state.selected_product = p
                    # Execute evaluation
                    st.session_state.current_product_eval = ProductRadar.evaluate_product(
                        product_name=p["name"],
                        category=p["category"],
                        product_type=p["product_type"],
                        cost_unit=p["cost_unit"],
                        target_price=p["target_price"],
                        wow_factor_score=p.get("wow_factor", 8),
                        pain_passion_score=p.get("pain_passion", 9),
                        offline_scarcity_score=p.get("offline_scarcity", 8),
                        has_size_variants=p.get("has_size_variants", False),
                        is_fragile=p.get("is_fragile", False),
                        is_heavy_or_bulky=p.get("is_heavy", False),
                        is_electric_or_battery_risk=p.get("is_battery", False),
                    )
                    # Log search telemetry to SQLite Knowledge Base
                    kb.log_search(
                        search_query=query_filter if query_filter else "Navegación por catálogo",
                        category_filter=cat_filter,
                        selected_product_name=p["name"]
                    )
                    st.session_state.active_step = STEPS[1]
                    st.rerun()

            st.markdown("---")

    # Add custom discovered product
    with st.expander("➕ **¿Encontraste un producto en TikTok / Spy Tools? Regístralo en el Catálogo**"):
        with st.form("add_custom_prod_form"):
            cp_name = st.text_input("Nombre del Producto", value="Mini Proyector Portátil HD")
            cp_cat = st.selectbox("Categoría", ProductCatalog.get_all_categories()[1:])
            cp_type = st.radio("Tipo", ["Evergreen", "Viral/Trend"], horizontal=True)
            col_cp1, col_cp2 = st.columns(2)
            with col_cp1:
                cp_cost = st.number_input("Costo Unitario Origen ($)", min_value=0.5, value=12.0)
                cp_price = st.number_input("Precio Venta Objetivo ($)", min_value=1.0, value=49.99)
            with col_cp2:
                cp_pain = st.text_input("Dolor o Necesidad Principal", value="ver series o películas en pantalla gigante sin gastar en TV cara")
                cp_ben = st.text_input("Beneficio Inmediato", value="proyectar cine en casa de 100 pulgadas en cualquier pared")
            
            cp_submit = st.form_submit_button("Guardar en Catálogo y Analizar")
            if cp_submit:
                new_p = ProductCatalog.add_custom_product({
                    "name": cp_name,
                    "category": cp_cat,
                    "product_type": cp_type,
                    "cost_unit": cp_cost,
                    "target_price": cp_price,
                    "core_pain": cp_pain,
                    "main_benefit": cp_ben,
                    "audience": "Familias y jóvenes amantes del cine",
                    "dropship_platform": "CJ Dropshipping / AliExpress",
                    "china_keywords": cp_name,
                    "description": f"{cp_name} - Solución para {cp_ben}",
                })
                st.session_state.selected_product = new_p
                st.session_state.current_product_eval = ProductRadar.evaluate_product(
                    product_name=new_p["name"],
                    category=new_p["category"],
                    product_type=new_p["product_type"],
                    cost_unit=new_p["cost_unit"],
                    target_price=new_p["target_price"],
                    wow_factor_score=8,
                    pain_passion_score=8,
                    offline_scarcity_score=8,
                    has_size_variants=False,
                    is_fragile=False,
                    is_heavy_or_bulky=False,
                    is_electric_or_battery_risk=False,
                )
                kb.log_search(search_query=cp_name, category_filter=cp_cat, selected_product_name=cp_name)
                st.session_state.active_step = STEPS[1]
                st.rerun()

# ==============================================================================
# PASO 2: RADAR & VALIDACIÓN DE 5 PILARES
# ==============================================================================
elif current_step == STEPS[1]:
    st.markdown("### 🎯 **Paso 2: Radar de Validación & Regla de los 5 Pilares**")
    st.caption("Filtra y valida la viabilidad financiera del producto antes de gastar en pauta.")

    active_p = st.session_state.selected_product

    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        st.markdown("#### 📝 **Parámetros del Producto Seleccionado**")
        p_name = st.text_input("Nombre del Producto", value=active_p["name"], key="radar_p_name")
        
        c_cat1, c_cat2 = st.columns(2)
        with c_cat1:
            categories_list = [
                "Salud & Ergonomía (Evergreen)",
                "Gadgets de Cocina / Hogar (Evergreen)",
                "Belleza & Cuidado Personal",
                "Organización & Limpieza",
                "Fitness & Deportes",
                "Viral TikTok / Gadgets Wow",
                "Accesorios de Oficina / Trabajo",
            ]
            default_cat_idx = categories_list.index(active_p["category"]) if active_p["category"] in categories_list else 0
            p_category = st.selectbox("Categoría / Nicho", categories_list, index=default_cat_idx, key="radar_p_cat")
        with c_cat2:
            default_type_idx = 0 if active_p["product_type"] == "Evergreen" else 1
            p_type = st.radio(
                "Naturaleza",
                ["Evergreen (Demanda 12 Meses)", "Viral / Trend (Tendencia TikTok)"],
                index=default_type_idx,
                horizontal=True,
                key="radar_p_type"
            )
            p_type_val = "Evergreen" if "Evergreen" in p_type else "Viral/Trend"

        st.markdown("---")
        st.markdown("#### 💰 **Economía Básica (Margen Mínimo 3X-5X)**")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            p_cost = st.number_input("Costo Unitario en Origen (COGS + Flete DS) [$]", min_value=0.5, value=float(active_p["cost_unit"]), step=0.50, key="radar_p_cost")
        with c_p2:
            p_price = st.number_input("Precio de Venta Objetivo al Público (PVP) [$]", min_value=1.0, value=float(active_p["target_price"]), step=1.0, key="radar_p_price")

        st.markdown("---")
        st.markdown("#### ⭐ **Pilares Cualitativos (1 a 10)**")
        c_q1, c_q2, c_q3 = st.columns(3)
        with c_q1:
            p_wow = st.slider("Efecto WOW (0-3s)", 1, 10, int(active_p.get("wow_factor", 8)), key="radar_p_wow")
        with c_q2:
            p_pain = st.slider("Dolor o Pasión", 1, 10, int(active_p.get("pain_passion", 9)), key="radar_p_pain")
        with c_q3:
            p_scarcity = st.slider("Escasez en Tienda Física", 1, 10, int(active_p.get("offline_scarcity", 8)), key="radar_p_scarcity")

        st.markdown("---")
        st.markdown("#### ⚠️ **Filtro de Riesgo Logístico**")
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            has_sizes = st.checkbox("Depende de talles complejos (Ropa/Calzado)", value=active_p.get("has_size_variants", False), key="radar_chk_sizes")
            is_fragile = st.checkbox("Material frágil (Vidrio/Cerámica)", value=active_p.get("is_fragile", False), key="radar_chk_fragile")
        with c_r2:
            is_heavy = st.checkbox("Pesado / Volumétrico (>1.5kg)", value=active_p.get("is_heavy", False), key="radar_chk_heavy")
            is_battery = st.checkbox("Baterías peligrosas sin certificar", value=active_p.get("is_battery", False), key="radar_chk_battery")

        if st.button("🔄 Recalcular Scoring de 5 Pilares", use_container_width=True):
            st.session_state.current_product_eval = ProductRadar.evaluate_product(
                product_name=p_name,
                category=p_category,
                product_type=p_type_val,
                cost_unit=p_cost,
                target_price=p_price,
                wow_factor_score=p_wow,
                pain_passion_score=p_pain,
                offline_scarcity_score=p_scarcity,
                has_size_variants=has_sizes,
                is_fragile=is_fragile,
                is_heavy_or_bulky=is_heavy,
                is_electric_or_battery_risk=is_battery,
            )
            st.rerun()

    eval_data = st.session_state.current_product_eval

    with col2:
        st.markdown("#### 🏁 **Resultado & Semáforo de Decisión**")
        
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("Multiplicador", f"{eval_data['multiplier']}X", f"{eval_data['gross_margin_pct']}% Margen")
        c_m2.metric("Score Global", f"{eval_data['total_score']} / 100")
        c_m3.metric("Nicho", eval_data["product_type"])

        v_class = "verdict-box-success" if "APROBADO" in eval_data["verdict"] else ("verdict-box-warning" if "DUDOSO" in eval_data["verdict"] else "verdict-box-error")
        st.markdown(f"""
        <div class="{v_class}">
            <h2 style="margin:0 0 8px 0; font-size:1.35rem;">{eval_data['verdict']}</h2>
            <p style="margin:0 0 10px 0; font-size:0.93rem;">{eval_data['verdict_summary']}</p>
            <div style="background: rgba(0,0,0,0.25); padding: 10px 14px; border-radius: 8px; font-size: 0.88rem;">
                <strong>Siguiente Acción Sugerida:</strong> {eval_data['action_recommendation']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 📊 **Desglose de Puntos por Pilar**")
        for pillar, score in eval_data["pillar_breakdown"].items():
            max_p = 30 if "30" in pillar else (25 if "25" in pillar else 15)
            pct = score / max_p
            st.write(f"**{pillar}**: `{score} pts`")
            st.progress(pct)

        if eval_data["strengths"]:
            st.markdown("##### ✅ **Puntos Fuertes**")
            for s in eval_data["strengths"]:
                st.write(f"• {s}")

        st.markdown("---")
        c_btn_a, c_btn_b = st.columns(2)
        with c_btn_a:
            if st.button("💾 Guardar en Memoria Histórica", use_container_width=True):
                product_id = kb.save_product_evaluation({
                    "product_name": eval_data["product_name"],
                    "category": eval_data["category"],
                    "product_type": eval_data["product_type"],
                    "cost_unit": eval_data["cost_unit"],
                    "target_price": eval_data["target_price"],
                    "multiplier": eval_data["multiplier"],
                    "total_score": eval_data["total_score"],
                    "verdict": eval_data["verdict"],
                    "status": "Aprobado" if "APROBADO" in eval_data["verdict"] else "En Revisión",
                    "notes": f"Score: {eval_data['total_score']}/100.",
                    "lessons_learned": eval_data["action_recommendation"],
                })
                st.success(f"¡Guardado (ID #{product_id})!")
        with c_btn_b:
            if st.button("➡️ Avanzar a Paso 3: Tienda Dropshipping", use_container_width=True, type="primary"):
                st.session_state.active_step = STEPS[2]
                st.rerun()

# ==============================================================================
# PASO 3: CREACIÓN DE TIENDA & DROPSHIPPING PASO A PASO
# ==============================================================================
elif current_step == STEPS[2]:
    st.markdown("### 🛍️ **Paso 3: Creación de Tienda & Publicación de Dropshipping**")
    st.caption("Configura la oferta mínima viable en Shopify / Tiendanube, conéctala con el proveedor de dropshipping y exporta la ficha lista para publicar.")

    eval_data = st.session_state.current_product_eval
    active_p = st.session_state.selected_product

    t_cpa_val = round((eval_data["target_price"] - eval_data["cost_unit"]) * 0.55, 2)
    roadmap = ValidationBlueprint.generate_roadmap(
        product_name=eval_data["product_name"],
        category=eval_data["category"],
        product_type=eval_data["product_type"],
        cost_unit=eval_data["cost_unit"],
        target_price=eval_data["target_price"],
        target_cpa=t_cpa_val,
    )

    col_plat1, col_plat2 = st.columns([1.2, 0.8])
    with col_plat1:
        st.markdown(f"""
        <div class="product-card" style="border-left: 5px solid #10b981;">
            <h4 style="color:#34d399; margin:0 0 6px 0;">🚚 Plataforma de Dropshipping Recomendada:</h4>
            <p style="font-size:1.15rem; font-weight:700; color:#ffffff; margin:0 0 6px 0;">{roadmap['recommended_platform']}</p>
            <p style="color:#cbd5e1; font-size:0.92rem; margin:0 0 6px 0;">{roadmap['platform_reason']}</p>
            <p style="color:#93c5fd; font-size:0.88rem; margin:0;"><strong>Integración sugerida:</strong> <code>{roadmap['integration_app']}</code></p>
        </div>
        """, unsafe_allow_html=True)
    with col_plat2:
        st.markdown("#### 🎯 **Métricas Clave de la Oferta**")
        st.metric("PVP Individual", f"${eval_data['target_price']:.2f}")
        st.metric("Bundle Doble (15% OFF)", f"${(eval_data['target_price']*0.85*2):.2f}")
        st.metric("Meta de Validación", "30 a 50 Pedidos en 7 días")

    st.markdown("---")
    st.markdown("#### 📦 **Ficha de Producto Lista para Publicar (CRO & Shopify Ready)**")
    
    listing = AICreativeFactory.generate_shopify_listing(
        product_name=eval_data["product_name"],
        category=eval_data["category"],
        target_audience=active_p.get("audience", "Compradores online"),
        core_pain=active_p.get("core_pain", "problemas diarios"),
        main_benefit=active_p.get("main_benefit", "solución rápida y efectiva"),
        target_price=eval_data["target_price"],
    )

    tab_pub1, tab_pub2, tab_pub3 = st.tabs([
        "📝 Ficha Formateada & Bundles",
        "📄 Código HTML / Markdown para Pegar en Shopify",
        "📥 Exportación CSV de Producto",
    ])

    with tab_pub1:
        st.markdown(f"##### **Título SEO de Alta Conversión:**")
        st.code(listing["seo_title"], language="text")

        st.markdown("##### **Viñetas de Beneficios Emocionales (Fórmula PAS):**")
        for b in listing["bullets"]:
            st.markdown(b)

        st.markdown("##### **Bundles de Oferta de Checkout:**")
        st.table(pd.DataFrame(listing["bundles"]))

        st.markdown("##### **Preguntas Frecuentes Antiobjecciones:**")
        for f in listing["faqs"]:
            with st.expander(f"❓ {f['q']}"):
                st.write(f['a'])

    with tab_pub2:
        html_desc = f"""<h2>{listing['seo_title']}</h2>
<p><strong>¿Cansado de lidiar con problemas tradicionales?</strong> Descubre la solución definitiva diseñada para ofrecerte resultados inmediatos desde el primer uso.</p>
<h3>✨ Beneficios Clave:</h3>
<ul>
"""
        for b in listing["bullets"]:
            clean_b = b.replace("**", "").replace("⚡ ", "").replace("🎯 ", "").replace("💎 ", "").replace("🚀 ", "").replace("🛡️ ", "")
            html_desc += f"  <li>{clean_b}</li>\n"
        html_desc += """</ul>
<h3>📦 Elige tu Paquete de Oferta:</h3>
<ul>
  <li><strong>1 Unidad:</strong> Precio regular de lanzamiento.</li>
  <li><strong>Paquete 2 Unidades:</strong> 15% de Descuento (Envío Prioritario).</li>
  <li><strong>Paquete 3 Unidades:</strong> 25% de Descuento + Envío Express GRATIS.</li>
</ul>
<h3>🛡️ Garantía Blindada de Satisfacción:</h3>
<p>Pruébalo durante 30 días sin riesgo. Si no cumple al 100% tus expectativas, te devolvemos tu dinero.</p>
"""
        st.code(html_desc, language="html")

    with tab_pub3:
        csv_data = pd.DataFrame([{
            "Handle": eval_data["product_name"].lower().replace(" ", "-"),
            "Title": listing["seo_title"],
            "Body (HTML)": html_desc,
            "Vendor": "Apex DTC Direct",
            "Type": eval_data["category"],
            "Tags": f"evergreen, viral, {eval_data['category'].lower()}",
            "Published": "TRUE",
            "Option1 Name": "Bundle",
            "Option1 Value": "1 Unidad",
            "Variant Price": eval_data["target_price"],
            "Variant Compare At Price": round(eval_data["target_price"] * 1.5, 2),
            "Variant Requires Shipping": "TRUE",
        }])
        st.dataframe(csv_data, use_container_width=True)
        csv_str = csv_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar CSV para Importar Directo en Shopify",
            data=csv_str,
            file_name=f"shopify_product_{eval_data['product_name'].lower().replace(' ', '_')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.markdown("---")
    if st.button("➡️ Avanzar a Paso 4: Fábrica de Creativos 3:2:2", use_container_width=True, type="primary"):
        st.session_state.active_step = STEPS[3]
        st.rerun()

# ==============================================================================
# PASO 4: FÁBRICA DE CREATIVOS 3:2:2
# ==============================================================================
elif current_step == STEPS[3]:
    st.markdown("### 🎨 **Paso 4: Fábrica de Creativos: Método Dinámico 3:2:2**")
    st.caption("Genera los 3 hooks de 0-3 segundos, demostraciones de producto, guiones y prompts para ElevenLabs y Midjourney.")

    eval_data = st.session_state.current_product_eval
    active_p = st.session_state.selected_product

    scripts = AICreativeFactory.generate_meta_322_scripts(
        product_name=eval_data["product_name"],
        category=eval_data["category"],
        target_audience=active_p.get("audience", "Compradores online"),
        core_pain=active_p.get("core_pain", "problemas cotidianos"),
        main_benefit=active_p.get("main_benefit", "solución rápida"),
        target_price=eval_data["target_price"],
    )

    st.markdown("#### 🎯 **Los 3 Hooks Visuales (0 a 3 Segundos - Scroll Stoppers)**")
    for h in scripts["hooks"]:
        st.markdown(f"""
        <div class="script-hook-card">
            <h4 style="color:#a5b4fc; margin:0 0 6px 0;">{h['id']}</h4>
            <p style="margin:0 0 6px 0;"><strong>🎬 Acción Visual:</strong> {h['visual_action']}</p>
            <p style="margin:0 0 6px 0;"><strong>🎙️ Locución:</strong> <em>"{h['voiceover_es']}"</em></p>
            <p style="margin:0; color:#38bdf8;"><strong>📱 Texto en Pantalla:</strong> <code>{h['on_screen_text']}</code></p>
        </div>
        """, unsafe_allow_html=True)

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.markdown("#### 📹 **Cuerpo A (Fórmula PAS)**")
        st.info(f"**Visual:**\n{scripts['bodies'][0]['visual_flow']}\n\n**Locución:**\n_{scripts['bodies'][0]['voiceover_es']}_")
    with col_b2:
        st.markdown("#### 📹 **Cuerpo B (Fórmula AIDA)**")
        st.info(f"**Visual:**\n{scripts['bodies'][1]['visual_flow']}\n\n**Locución:**\n_{scripts['bodies'][1]['voiceover_es']}_")

    st.markdown("#### ⚡ **Los 2 Call To Action (Últimos 5 Segundos)**")
    c_c1, c_c2 = st.columns(2)
    with c_c1:
        st.success(f"**{scripts['ctas'][0]['id']}**\n\n• **Overlay:** `{scripts['ctas'][0]['on_screen_text']}`\n• **Voz:** _{scripts['ctas'][0]['voiceover_es']}_")
    with c_c2:
        st.success(f"**{scripts['ctas'][1]['id']}**\n\n• **Overlay:** `{scripts['ctas'][1]['on_screen_text']}`\n• **Voz:** _{scripts['ctas'][1]['voiceover_es']}_")

    st.markdown("---")
    st.markdown("#### 🤖 **Prompts de IA Listos para Copiar**")
    prompts = AICreativeFactory.generate_ai_prompts(
        product_name=eval_data["product_name"],
        category=eval_data["category"],
        main_benefit=active_p.get("main_benefit", "solución rápida"),
    )
    c_pr1, c_pr2 = st.columns(2)
    with c_pr1:
        st.markdown("##### 🎙️ ElevenLabs (Locución):")
        st.code(prompts["elevenlabs"], language="text")
    with c_pr2:
        st.markdown("##### 📸 Midjourney v6 (Fotografía Publicitaria):")
        st.code(prompts["midjourney"], language="text")

    st.markdown("---")
    if st.button("➡️ Avanzar a Paso 5: Control de Pauta (Kill / Scale)", use_container_width=True, type="primary"):
        st.session_state.active_step = STEPS[4]
        st.rerun()

# ==============================================================================
# PASO 5: CONTROL DE PAUTA (KILL / SCALE)
# ==============================================================================
elif current_step == STEPS[4]:
    st.markdown("### 📊 **Paso 5: Control de Pauta & Motor Kill / Scale**")
    st.caption("Supervisa los anuncios de prueba y toma decisiones algorítmicas sin dudar.")

    eval_data = st.session_state.current_product_eval

    c_ad_p1, c_ad_p2 = st.columns([1, 1.2])

    with c_ad_p1:
        st.markdown("#### 🧮 **Guardarraíles Financieros**")
        ads_price = st.number_input("Precio de Venta ($)", min_value=5.0, value=float(eval_data["target_price"]), step=1.0)
        ads_cost = st.number_input("Costo Unitario Total ($)", min_value=1.0, value=float(eval_data["cost_unit"]), step=0.5)
        ads_margin_req = st.slider("Margen Neto Objetivo (%)", 10, 40, 25)
        
        financials = AdsAnalytics.calculate_targets(
            sale_price=ads_price,
            cost_unit=ads_cost,
            gateway_fee_pct=3.5,
            desired_net_margin_pct=float(ads_margin_req),
        )

        c_fin1, c_fin2 = st.columns(2)
        c_fin1.metric("Break-Even ROAS", f"{financials['be_roas']}x")
        c_fin2.metric("CPA Objetivo", f"${financials['target_cpa']}")

    with c_ad_p2:
        st.markdown("#### ⚡ **Diagnóstico de Anuncio en Vivo**")
        c_sim1, c_sim2 = st.columns(2)
        with c_sim1:
            sim_name = st.text_input("Campaña / Adset", value=f"Test_{eval_data['product_name'][:15]}_Hook1")
            sim_spend = st.number_input("Gasto Acumulado ($)", min_value=0.0, value=22.50, step=2.5)
            sim_impressions = st.number_input("Impresiones", min_value=100, value=1250, step=100)
        with c_sim2:
            sim_clicks = st.number_input("Clics en el Enlace", min_value=0, value=32, step=1)
            sim_atc = st.number_input("Añadidos al Carrito (ATC)", min_value=0, value=2, step=1)
            sim_purchases = st.number_input("Compras Registradas", min_value=0, value=1, step=1)

        sim_revenue = sim_purchases * ads_price
        analysis = AdsAnalytics.analyze_ad_performance(
            ad_name=sim_name,
            spend=sim_spend,
            impressions=sim_impressions,
            link_clicks=sim_clicks,
            add_to_carts=sim_atc,
            purchases=sim_purchases,
            revenue=sim_revenue,
            target_cpa=financials["target_cpa"],
            be_roas=financials["be_roas"],
        )

        ad_v_class = "verdict-box-success" if "ESCALAR" in analysis["status"] else ("verdict-box-error" if "KILL" in analysis["status"] else "verdict-box-warning")
        st.markdown(f"""
        <div class="{ad_v_class}" style="margin-top:10px;">
            <h3 style="margin:0 0 6px 0;">{analysis['status']}</h3>
            <p style="margin:0; font-size: 0.95rem;"><strong>Motivo:</strong> {analysis['decision_label']} - {analysis['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("➡️ Avanzar a Paso 6: Importación DDP & Fábricas", use_container_width=True, type="primary"):
        st.session_state.active_step = STEPS[5]
        st.rerun()

# ==============================================================================
# PASO 6: IMPORTACIÓN DDP & FÁBRICAS EN CHINA
# ==============================================================================
elif current_step == STEPS[5]:
    st.markdown("### 🚢 **Paso 6: Importación DDP & Sourcing en Fábrica**")
    st.caption("Una vez validadas las primeras 30-50 ventas en dropshipping, salta a la importación en lote para duplicar tu margen neto.")

    eval_data = st.session_state.current_product_eval
    active_p = st.session_state.selected_product

    c_sh1, c_sh2 = st.columns([1, 1.2])
    with c_sh1:
        st.markdown("#### ⚙️ **Parámetros del Lote**")
        sc_sale_price = st.number_input("Precio de Venta ($)", value=float(eval_data["target_price"]), min_value=1.0)
        sc_ds_cogs = st.number_input("Costo Unitario en Dropshipping ($)", value=float(eval_data["cost_unit"]), min_value=0.5)
        sc_fob = st.number_input("Costo Unitario Fábrica FOB ($)", value=round(eval_data["cost_unit"] * 0.35, 2), min_value=0.1)
        sc_freight = st.number_input("Flete DDP por Unidad ($)", value=1.80, min_value=0.1)
        sc_packaging = st.number_input("Empaque Private Label ($)", value=0.75, min_value=0.0)
        sc_3pl = st.number_input("Fulfillment 3PL Local ($)", value=3.20, min_value=0.0)
        sc_cpa = st.number_input("CPA Promedio de Pauta ($)", value=12.00, min_value=0.0)
        sc_units = st.select_slider("Tamaño del Lote", options=[100, 300, 500, 1000, 2000], value=500)

    with c_sh2:
        st.markdown("#### 📊 **Multiplicación de Ganancia**")
        margin_data = SourcingHub.calculate_margin_jump(
            sale_price=sc_sale_price,
            dropship_cogs_shipping=sc_ds_cogs,
            factory_fob_unit=sc_fob,
            ddp_shipping_unit=sc_freight,
            packaging_branding_unit=sc_packaging,
            local_3pl_pick_pack=sc_3pl,
            payment_gateway_pct=3.5,
            target_cpa=sc_cpa,
            units_batch=sc_units,
        )

        st.markdown(f"""
        <div class="verdict-box-success">
            <h3 style="margin:0 0 8px 0;">🚀 Impacto en Lote de {sc_units} Unidades</h3>
            <p style="margin:0 0 6px 0; font-size:1.05rem;">
                • Ganancia Neta Dropshipping: <strong>${margin_data['dropship']['batch_profit']:,.2f}</strong><br>
                • Ganancia Neta Importación DDP: <strong>${margin_data['bulk_ddp']['batch_profit']:,.2f}</strong><br>
                • <strong>Beneficio Extra en Mano:</strong> <span style="font-size:1.25rem; color:#34d399;">+${margin_data['comparison']['extra_profit_batch']:,.2f} USD (+{margin_data['comparison']['profit_increase_pct']}%)</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### ✉️ **Mensaje RFQ para Fábricas en China (Alibaba / 1688)**")
    rfq_text = SourcingHub.generate_rfq_message(
        company_name="Apex DTC Direct Group",
        contact_name="Procurement Director",
        product_name=active_p.get("china_keywords", eval_data["product_name"]),
        target_destination_country="United States (3PL Warehouse)",
        custom_logo=True,
        custom_box=True,
        barcode_labeling=True,
    )
    st.code(rfq_text, language="text")

    st.markdown("---")
    if st.button("➡️ Avanzar a Paso 7: Memoria & Aprendizaje del Sistema", use_container_width=True, type="primary"):
        st.session_state.active_step = STEPS[6]
        st.rerun()

# ==============================================================================
# PASO 7: MEMORIA & APRENDIZAJE CONTINUO
# ==============================================================================
elif current_step == STEPS[6]:
    st.markdown("### 🧠 **Paso 7: Memoria Operativa & Sistema de Aprendizaje Continuo**")
    st.caption("El sistema almacena el historial de búsquedas, productos validados y reglas operativas para mejorar sus recomendaciones continuamente.")

    sub_m1, sub_m2, sub_m3 = st.tabs([
        "📈 Inteligencia & Telemetría de Búsquedas",
        "🗂️ Historial de Productos Validados",
        "📜 Reglas & Principios Operativos",
    ])

    with sub_m1:
        st.markdown("#### 🔍 **Patrones de Búsqueda y Nichos más Explorados**")
        stats = kb.get_search_learning_insights()
        
        c_st1, c_st2 = st.columns(2)
        with c_st1:
            st.markdown("##### 🏆 Categorías con Mayor Interés:")
            if stats["top_categories"]:
                df_top_cats = pd.DataFrame(stats["top_categories"])
                df_top_cats.columns = ["Categoría", "Consultas"]
                st.dataframe(df_top_cats, use_container_width=True)
            else:
                st.info("Aún no hay búsquedas suficientes registradas.")

        with c_st2:
            st.markdown("##### 🚀 Productos Más Analizados:")
            if stats["top_analyzed_products"]:
                df_top_prods = pd.DataFrame(stats["top_analyzed_products"])
                df_top_prods.columns = ["Producto", "Veces Analizado"]
                st.dataframe(df_top_prods, use_container_width=True)
            else:
                st.info("Aún no hay análisis registrados.")

        st.markdown("##### 🕒 Registro Reciente de Telemetría:")
        if stats["recent_logs"]:
            st.dataframe(pd.DataFrame(stats["recent_logs"])[["search_query", "category_filter", "selected_product_name", "created_at"]], use_container_width=True)

    with sub_m2:
        products = kb.get_all_products()
        if not products:
            st.info("Aún no hay productos guardados.")
        else:
            df_prods = pd.DataFrame(products)
            st.dataframe(
                df_prods[["id", "product_name", "category", "product_type", "multiplier", "total_score", "verdict", "status", "created_at"]],
                use_container_width=True,
            )

    with sub_m3:
        rules = kb.get_all_rules()
        for r in rules:
            with st.expander(f"📌 [{r['category']}] {r['title']} — {r['author']}"):
                st.markdown(f"**Regla:** {r['rule']}")
                st.info(f"💡 {r['actionable_tip']}")
