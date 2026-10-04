"""
E-Commerce Automation OS (ecom-automation-os)
Executive Interactive Dashboard for Product Discovery, Fast Validation, 3:2:2 Creatives, Media Buying & Sourcing Scale.
"""

import streamlit as st
import pandas as pd
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
        padding: 24px 32px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 24px;
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
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.8) 0%, rgba(6, 95, 70, 0.4) 100%);
        border: 1px solid #10b981;
        border-radius: 14px;
        padding: 20px 24px;
        color: #ecfdf5;
    }
    .verdict-box-warning {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.8) 0%, rgba(146, 64, 14, 0.4) 100%);
        border: 1px solid #f59e0b;
        border-radius: 14px;
        padding: 20px 24px;
        color: #fffbeb;
    }
    .verdict-box-error {
        background: linear-gradient(135deg, rgba(136, 19, 55, 0.8) 0%, rgba(159, 18, 57, 0.4) 100%);
        border: 1px solid #f43f5e;
        border-radius: 14px;
        padding: 20px 24px;
        color: #fff1f2;
    }
    
    .roadmap-phase-card {
        background: rgba(30, 41, 59, 0.65);
        border-left: 5px solid #6366f1;
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 16px;
    }
    
    .script-hook-card {
        background: #1e293b;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0px 0px;
        padding: 10px 18px;
        font-weight: 600;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialize Knowledge Base & Session State ---
kb = KnowledgeBase()

if "selected_product" not in st.session_state:
    # Default to first product in catalog
    st.session_state.selected_product = CURATED_PRODUCTS[0]

if "current_product_eval" not in st.session_state:
    st.session_state.current_product_eval = None

# --- Sidebar Header & Navigation Info ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1556742049-0a67e557b6f6?w=400&auto=format&fit=crop&q=80", use_container_width=True)
    st.markdown("## ⚡ **E-Com Automation OS**")
    st.caption("Sistema integral: Búsqueda ➔ Validación 5 Pilares ➔ Dropshipping ➔ Escalamiento DDP.")
    
    st.markdown("---")
    st.markdown("### 🎯 **Enfoques de Nicho**")
    st.markdown("""
    - 🚀 **Trend-Driven:** Scroll-stoppers (0-3s), efecto WOW, TikTok / Meta Ads.
    - 🌲 **Evergreen (12 Meses):** Salud/Postura, Cocina/Hogar, Organización, Cuidado Personal.
    """)
    
    st.markdown("---")
    # Quick DB statistics
    products_history = kb.get_all_products()
    approved_count = sum(1 for p in products_history if "APROBADO" in p.get("verdict", ""))
    st.markdown("### 📊 **Métricas del Workspace**")
    col_sb1, col_sb2 = st.columns(2)
    col_sb1.metric("Evaluados", len(products_history))
    col_sb2.metric("Aprobados", approved_count)

    st.markdown("---")
    st.caption("v1.2.0 • Production Ready (White-Label)")

# --- Top Header ---
st.markdown("""
<div class="main-header">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
        <div>
            <span class="badge-tag badge-trend">🔥 Trend-Driven</span>
            <span class="badge-tag badge-evergreen">🌲 Evergreen Engine</span>
            <span class="badge-tag badge-pro">⚡ DTC Scale Framework</span>
            <h1 style="color: #ffffff; margin: 10px 0 6px 0; font-size: 2.1rem; font-weight: 800;">
                E-Commerce Automation OS
            </h1>
            <p style="color: #94a3b8; margin: 0; font-size: 0.98rem;">
                Pipeline integral: <strong>Buscador por Categoría</strong> ➔ <strong>Radar de 5 Pilares</strong> ➔ <strong>Blueprint Dropshipping a DDP</strong> ➔ <strong>Fábrica Creativa 3:2:2</strong> ➔ <strong>Control de Pauta</strong>
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Executive Tabs ---
tab_search, tab_radar, tab_roadmap, tab_creatives, tab_ads, tab_sourcing, tab_db = st.tabs([
    "🔍 Buscador & Catálogo",
    "🎯 Radar & Validación",
    "🗺️ Roadmap Dropship ➔ DDP",
    "🎨 Fábrica de Creativos (3:2:2)",
    "📊 Control de Pauta (Kill / Scale)",
    "🚢 Importación & Sourcing DDP",
    "🧠 Memoria & Lecciones (DB)",
])

# ==============================================================================
# TAB 0: BUSCADOR & CATÁLOGO POR CATEGORÍA
# ==============================================================================
with tab_search:
    st.markdown("### 🔍 **Buscador & Explorador de Oportunidades por Categoría**")
    st.caption("Explora productos pre-investigados con alto potencial de margen y carga cualquiera de ellos con 1 clic al Radar de Validación.")

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
                        <h3 style="color:#ffffff; margin:8px 0 4px 0; font-size:1.25rem;">{p['name']}</h3>
                        <p style="color:#94a3b8; font-size:0.92rem; margin:0 0 10px 0;">{p['description']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_det1, c_det2, c_det3, c_det4, c_det5 = st.columns([1, 1, 1, 1.8, 1.2])
            c_det1.metric("Costo Fábrica", f"${p['cost_unit']:.2f}")
            c_det2.metric("PVP Sugerido", f"${p['target_price']:.2f}")
            c_det3.metric("Multiplicador", f"{mult}X")
            with c_det4:
                st.caption(f"**🚚 Plataforma DS:** {p['dropship_platform']}")
                st.caption(f"**🇨🇳 Búsqueda 1688/Alibaba:** `{p['china_keywords']}`")
            with c_det5:
                if st.button(f"📥 Analizar en Radar", key=f"btn_load_{p['id']}", use_container_width=True, type="primary"):
                    st.session_state.selected_product = p
                    # Trigger automatic evaluation
                    st.session_state.current_product_eval = ProductRadar.evaluate_product(
                        product_name=p["name"],
                        category=p["category"],
                        product_type=p["product_type"],
                        cost_unit=p["cost_unit"],
                        target_price=p["target_price"],
                        wow_factor_score=p["wow_factor"],
                        pain_passion_score=p["pain_passion"],
                        offline_scarcity_score=p["offline_scarcity"],
                        has_size_variants=p["has_size_variants"],
                        is_fragile=p["is_fragile"],
                        is_heavy_or_bulky=p["is_heavy"],
                        is_electric_or_battery_risk=p["is_battery"],
                    )
                    st.success(f"¡'{p['name']}' cargado al Radar de Validación y Roadmap!")
                    st.rerun()
            st.markdown("---")

# ==============================================================================
# TAB 1: RADAR & VALIDACIÓN (5 PILARES)
# ==============================================================================
with tab_radar:
    st.markdown("### 🎯 **Radar de Scoring: Regla de los 5 Pilares**")
    st.caption("Filtra productos con viabilidad matemática antes de gastar un solo dólar en creativos o publicidad.")

    active_p = st.session_state.selected_product

    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        st.markdown("#### 📝 **Datos del Producto a Validar**")
        p_name = st.text_input("Nombre del Producto", value=active_p["name"])
        
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
            p_category = st.selectbox("Categoría / Nicho", categories_list, index=default_cat_idx)
        with c_cat2:
            default_type_idx = 0 if active_p["product_type"] == "Evergreen" else 1
            p_type = st.radio(
                "Naturaleza del Producto",
                ["Evergreen (Demanda 12 Meses)", "Viral / Trend (Tendencia TikTok)"],
                index=default_type_idx,
                horizontal=True,
            )
            p_type_val = "Evergreen" if "Evergreen" in p_type else "Viral/Trend"

        st.markdown("---")
        st.markdown("#### 💰 **Economía Básica (Margen Mínimo 3X-5X)**")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            p_cost = st.number_input("Costo Unitario en Origen (COGS + Flete DS) [$]", min_value=0.5, value=float(active_p["cost_unit"]), step=0.50)
        with c_p2:
            p_price = st.number_input("Precio de Venta Objetivo al Público (PVP) [$]", min_value=1.0, value=float(active_p["target_price"]), step=1.0)

        st.markdown("---")
        st.markdown("#### ⭐ **Pilares Cualitativos (Puntuación 1 a 10)**")
        c_q1, c_q2, c_q3 = st.columns(3)
        with c_q1:
            p_wow = st.slider("Efecto WOW (0-3s)", 1, 10, int(active_p.get("wow_factor", 8)), help="Poder de llamar la atención de inmediato en el feed.")
        with c_q2:
            p_pain = st.slider("Dolor o Pasión", 1, 10, int(active_p.get("pain_passion", 9)), help="Intensidad de la molestia que resuelve o deseo apasionado.")
        with c_q3:
            p_scarcity = st.slider("Escasez en Tienda Física", 1, 10, int(active_p.get("offline_scarcity", 8)), help="Dificultad de comprarlo en el supermercado común.")

        st.markdown("---")
        st.markdown("#### ⚠️ **Filtro de Riesgo Logístico & Devoluciones**")
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            has_sizes = st.checkbox("Depende de talles complejos (Ropa/Calzado)", value=active_p.get("has_size_variants", False))
            is_fragile = st.checkbox("Material frágil (Vidrio/Cerámica rompible)", value=active_p.get("is_fragile", False))
        with c_r2:
            is_heavy = st.checkbox("Pesado o Volumétrico (> 1.5 kg)", value=active_p.get("is_heavy", False))
            is_battery = st.checkbox("Baterías peligrosas / No homologadas", value=active_p.get("is_battery", False))

        btn_eval = st.button("🚀 Ejecutar Scoring de 5 Pilares", use_container_width=True, type="primary")

    # Evaluate logic
    if btn_eval or st.session_state.current_product_eval is None:
        eval_result = ProductRadar.evaluate_product(
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
        st.session_state.current_product_eval = eval_result

    eval_data = st.session_state.current_product_eval

    with col2:
        st.markdown("#### 🏁 **Resultado & Semáforo de Decisión**")
        
        # Metric Cards Header
        c_m1, c_m2, c_m3 = st.columns(3)
        c_m1.metric("Multiplicador", f"{eval_data['multiplier']}X", f"{eval_data['gross_margin_pct']}% Margen")
        c_m2.metric("Score Global", f"{eval_data['total_score']} / 100")
        c_m3.metric("Nicho", eval_data["product_type"])

        # Verdict Banner
        v_class = "verdict-box-success" if "APROBADO" in eval_data["verdict"] else ("verdict-box-warning" if "DUDOSO" in eval_data["verdict"] else "verdict-box-error")
        st.markdown(f"""
        <div class="{v_class}">
            <h2 style="margin:0 0 8px 0; font-size:1.4rem;">{eval_data['verdict']}</h2>
            <p style="margin:0 0 10px 0; font-size:0.95rem;">{eval_data['verdict_summary']}</p>
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
            st.markdown("##### ✅ **Puntos Fuertes Detectados**")
            for s in eval_data["strengths"]:
                st.write(f"• {s}")

        if eval_data["red_flags"]:
            st.markdown("##### ⚠️ **Puntos Críticos / Red Flags**")
            for rf in eval_data["red_flags"]:
                st.write(f"• 🚩 {rf}")

        # Save to Database Button
        st.markdown("---")
        if st.button("💾 Guardar Evaluación en Memoria Histórica", use_container_width=True):
            product_id = kb.save_product_evaluation({
                "product_name": eval_data["product_name"],
                "category": eval_data["category"],
                "product_type": eval_data["product_type"],
                "cost_unit": eval_data["cost_unit"],
                "target_price": eval_data["target_price"],
                "multiplier": eval_data["multiplier"],
                "total_score": eval_data["total_score"],
                "verdict": eval_data["verdict"],
                "status": "Aprobado" if "APROBADO" in eval_data["verdict"] else ("En Revisión" if "DUDOSO" in eval_data["verdict"] else "Descartado"),
                "notes": f"Score 5 Pilares: {eval_data['total_score']}/100.",
                "lessons_learned": eval_data["action_recommendation"],
            })
            st.success(f"¡Guardado con éxito en Base de Datos (ID #{product_id})!")

# ==============================================================================
# TAB 2: ROADMAP DE VALIDACIÓN (DROPSHIPPING ➔ ESCALAMIENTO DDP)
# ==============================================================================
with tab_roadmap:
    st.markdown("### 🗺️ **Roadmap de Validación: Dropshipping ➔ Escalamiento DDP**")
    st.caption("Guía operativa paso a paso para vender con la plataforma de dropshipping correcta, validar tracción en masa y saltar a la importación en fábrica.")

    # Target CPA estimation for calculations
    t_cpa_val = round((eval_data["target_price"] - eval_data["cost_unit"]) * 0.55, 2) if eval_data else 15.00

    c_rd1, c_rd2 = st.columns([1.5, 1])
    with c_rd1:
        rd_market = st.selectbox(
            "Mercado Objetivo de Venta",
            [
                "Estados Unidos / Global (Tráfico en Inglés)",
                "España / Europa (Envío Express)",
                "LATAM (Modelo Contraentrega / Cash On Delivery)",
                "México / Colombia / Chile / Perú (Local Dropshipping)",
            ]
        )
    with c_rd2:
        st.metric("CPA de Prueba Estimado", f"${t_cpa_val:.2f}", f"Presupuesto 3X: ${(t_cpa_val*3):.2f}/día")

    roadmap_data = ValidationBlueprint.generate_roadmap(
        product_name=eval_data["product_name"] if eval_data else "Producto Validado",
        category=eval_data["category"] if eval_data else "General",
        product_type=eval_data["product_type"] if eval_data else "Evergreen",
        cost_unit=eval_data["cost_unit"] if eval_data else 10.0,
        target_price=eval_data["target_price"] if eval_data else 39.99,
        target_cpa=t_cpa_val,
        target_market=rd_market,
    )

    st.markdown(f"""
    <div class="product-card" style="border-left: 5px solid #10b981; margin-top: 10px;">
        <h4 style="color:#34d399; margin:0 0 6px 0;">🚀 Plataforma de Dropshipping Recomendada para este Producto:</h4>
        <p style="font-size:1.1rem; font-weight:700; color:#ffffff; margin:0 0 6px 0;">{roadmap_data['recommended_platform']}</p>
        <p style="color:#cbd5e1; font-size:0.92rem; margin:0 0 6px 0;">{roadmap_data['platform_reason']}</p>
        <p style="color:#93c5fd; font-size:0.88rem; margin:0;"><strong>Stack de Integración:</strong> <code>{roadmap_data['integration_app']}</code></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📋 **Las 3 Fases del Protocolo de Ejecución:**")

    for phase in roadmap_data["phases"]:
        st.markdown(f"""
        <div class="roadmap-phase-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="color:#ffffff; margin:0;">{phase['phase_number']}: {phase['phase_title']}</h3>
                <span class="badge-tag badge-pro">{phase['badge']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        for s in phase["steps"]:
            with st.expander(f"📌 **{s['step_title']}**", expanded=True):
                st.markdown(s["details"])
                st.info(f"💡 **Consejo Operativo Clave:** {s['tip']}")

# ==============================================================================
# TAB 3: FÁBRICA DE CREATIVOS (MÉTODO 3:2:2 & SHOPIFY CRO)
# ==============================================================================
with tab_creatives:
    st.markdown("### 🎨 **Fábrica de Creativos: Método Dinámico 3:2:2 & Shopify CRO**")
    st.caption("Genera hooks visuales de alta retención, guiones de video, fichas de conversión para tienda y prompts de IA.")

    # Prefill from selected product
    default_pname = active_p.get("name", "Corrector Lumbar Ergonómico Pro")
    default_price = float(active_p.get("target_price", 39.99))
    default_aud = active_p.get("audience", "Personas con dolor de espalda y trabajadores remotos")
    default_pain = active_p.get("core_pain", "dolor lumbar crónico y mala postura")
    default_ben = active_p.get("main_benefit", "aliviar la tensión en la columna y corregir la postura")

    c_cr1, c_cr2, c_cr3 = st.columns(3)
    with c_cr1:
        cr_product = st.text_input("Producto para Creativos", value=default_pname)
    with c_cr2:
        cr_audience = st.text_input("Audiencia / Cliente Ideal", value=default_aud)
    with c_cr3:
        cr_price = st.number_input("Precio de Venta ($)", value=default_price, min_value=1.0)

    c_cr4, c_cr5 = st.columns(2)
    with c_cr4:
        cr_pain = st.text_input("Dolor Principal que Resuelve", value=default_pain)
    with c_cr5:
        cr_benefit = st.text_input("Beneficio Clave Inmediato", value=default_ben)

    st.markdown("---")

    sub_tab1, sub_tab2, sub_tab3 = st.tabs([
        "🎬 Guiones de Video 3:2:2 (Meta Ads)",
        "🛍️ Ficha Shopify & Bundles CRO",
        "🤖 Prompts para ElevenLabs / Midjourney / Flair",
    ])

    # 1. Video Scripts 3:2:2
    with sub_tab1:
        scripts = AICreativeFactory.generate_meta_322_scripts(
            product_name=cr_product,
            category="E-commerce",
            target_audience=cr_audience,
            core_pain=cr_pain,
            main_benefit=cr_benefit,
            target_price=cr_price,
        )

        st.markdown("#### 🎯 **Los 3 Hooks Visuales (0 a 3 Segundos - Scroll Stoppers)**")
        for h in scripts["hooks"]:
            st.markdown(f"""
            <div class="script-hook-card">
                <h4 style="color:#a5b4fc; margin:0 0 6px 0;">{h['id']}</h4>
                <p style="margin:0 0 6px 0;"><strong>🎬 Acción Visual:</strong> {h['visual_action']}</p>
                <p style="margin:0 0 6px 0;"><strong>🎙️ Voz en Off (Audio):</strong> <em>"{h['voiceover_es']}"</em></p>
                <p style="margin:0; color:#38bdf8;"><strong>📱 Texto en Pantalla:</strong> <code>{h['on_screen_text']}</code></p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 📹 **Las 2 Variaciones de Cuerpo / Demostración (3 a 20 Segundos)**")
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            b1 = scripts["bodies"][0]
            st.markdown(f"##### **{b1['id']}**")
            st.info(f"**Flujo Visual:**\n\n{b1['visual_flow']}\n\n**Locución:**\n\n_{b1['voiceover_es']}_")
        with col_b2:
            b2 = scripts["bodies"][1]
            st.markdown(f"##### **{b2['id']}**")
            st.info(f"**Flujo Visual:**\n\n{b2['visual_flow']}\n\n**Locución:**\n\n_{b2['voiceover_es']}_")

        st.markdown("#### ⚡ **Los 2 Call To Action (Últimos 5 Segundos)**")
        col_cta1, col_cta2 = st.columns(2)
        with col_cta1:
            c1 = scripts["ctas"][0]
            st.success(f"**{c1['id']}**\n\n• **Visual:** {c1['visual_flow']}\n\n• **Voz:** _{c1['voiceover_es']}_\n\n• **Overlay:** `{c1['on_screen_text']}`")
        with col_cta2:
            c2 = scripts["ctas"][1]
            st.success(f"**{c2['id']}**\n\n• **Visual:** {c2['visual_flow']}\n\n• **Voz:** _{c2['voiceover_es']}_\n\n• **Overlay:** `{c2['on_screen_text']}`")

    # 2. Shopify Listing & Bundles
    with sub_tab2:
        shopify = AICreativeFactory.generate_shopify_listing(
            product_name=cr_product,
            category="Salud",
            target_audience=cr_audience,
            core_pain=cr_pain,
            main_benefit=cr_benefit,
            target_price=cr_price,
        )

        st.markdown(f"#### 🏷️ **Título SEO de Alta Conversión**")
        st.code(shopify["seo_title"], language="markdown")

        st.markdown("#### ✨ **Viñetas de Beneficios Emocionales (Fórmula PAS)**")
        for b in shopify["bullets"]:
            st.markdown(b)

        st.markdown("---")
        st.markdown("#### 📦 **Estructura de Bundles para Maximizar Ticket Promedio (AOV)**")
        df_bundles = pd.DataFrame(shopify["bundles"])
        st.table(df_bundles)

        st.markdown("#### ❓ **FAQ Antiobjecciones para Página de Producto**")
        for f in shopify["faqs"]:
            with st.expander(f"**{f['q']}**"):
                st.write(f['a'])

    # 3. AI Prompts Matrix
    with sub_tab3:
        prompts = AICreativeFactory.generate_ai_prompts(
            product_name=cr_product,
            category="E-commerce",
            main_benefit=cr_benefit,
        )

        st.markdown("#### 🎙️ **Prompt para ElevenLabs (Voz en Off Ultra Realista)**")
        st.code(prompts["elevenlabs"], language="text")

        st.markdown("#### 📸 **Prompt para Midjourney v6 (Fotografía de Producto Publicitaria)**")
        st.code(prompts["midjourney"], language="text")

        st.markdown("#### 🖼️ **Prompt para Flair.ai (Fondos de Estudio para E-commerce)**")
        st.code(prompts["flair_ai"], language="text")

# ==============================================================================
# TAB 4: CONTROL DE PAUTA (ADS ANALYTICS & KILL/SCALE ENGINE)
# ==============================================================================
with tab_ads:
    st.markdown("### 📊 **Control de Pauta & Algoritmo de Decisión (Kill / Scale)**")
    st.caption("Calcula automáticamente tu Break-Even y aplica reglas sistemáticas de medios para no quemar presupuesto.")

    c_ad_p1, c_ad_p2 = st.columns([1, 1.2])

    with c_ad_p1:
        st.markdown("#### 🧮 **1. Guardarraíles Financieros**")
        ads_price = st.number_input("Precio de Venta ($)", min_value=5.0, value=float(eval_data["target_price"]) if eval_data else 39.99, step=1.0, key="ads_calc_price")
        ads_cost = st.number_input("Costo Unitario Total ($)", min_value=1.0, value=float(eval_data["cost_unit"]) if eval_data else 9.50, step=0.5, key="ads_calc_cost")
        ads_margin_req = st.slider("Margen Neto Objetivo Mínimo (%)", 10, 40, 25, help="Porcentaje de ganancia limpia después de pauta publicitaria.")
        
        financials = AdsAnalytics.calculate_targets(
            sale_price=ads_price,
            cost_unit=ads_cost,
            gateway_fee_pct=3.5,
            desired_net_margin_pct=float(ads_margin_req),
        )

        st.markdown("##### 🎯 **Métricas Clave de Punto de Equilibrio:**")
        c_fin1, c_fin2 = st.columns(2)
        c_fin1.metric("Break-Even ROAS", f"{financials['be_roas']}x", "Mínimo para no perder")
        c_fin2.metric("CPA Objetivo", f"${financials['target_cpa']}", f"Ganancia ${financials['desired_net_profit_per_order']}/ud")

    with c_ad_p2:
        st.markdown("#### ⚡ **2. Diagnóstico de Anuncio / Conjunto en Vivo**")
        
        c_sim1, c_sim2 = st.columns(2)
        with c_sim1:
            sim_name = st.text_input("Nombre de Campaña / Adset", value="Test_322_Hook1_Intereses_Espalda")
            sim_spend = st.number_input("Gasto Acumulado ($)", min_value=0.0, value=22.50, step=2.5)
            sim_impressions = st.number_input("Impresiones", min_value=100, value=1250, step=100)
        with c_sim2:
            sim_clicks = st.number_input("Clics en el Enlace (Link Clicks)", min_value=0, value=32, step=1)
            sim_atc = st.number_input("Añadidos al Carrito (ATC)", min_value=0, value=2, step=1)
            sim_purchases = st.number_input("Compras Registradas", min_value=0, value=1, step=1)

        sim_revenue = sim_purchases * ads_price

        # Run Live Diagnosis
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

        st.markdown("---")
        st.markdown("#### 🏁 **Diagnóstico & Decisión Algorítmica:**")
        
        c_dec1, c_dec2, c_dec3 = st.columns(3)
        c_dec1.metric("ROAS Real", f"{analysis['real_roas']}x", f"BE: {analysis['be_roas']}x")
        c_dec2.metric("CPA Real", f"${analysis['real_cpa']}", f"Target: ${analysis['target_cpa']}")
        c_dec3.metric("CTR Enlace", f"{analysis['ctr_link']}%", "Min 1.0%")

        # Banner
        ad_v_class = "verdict-box-success" if "ESCALAR" in analysis["status"] else ("verdict-box-error" if "KILL" in analysis["status"] else "verdict-box-warning")
        st.markdown(f"""
        <div class="{ad_v_class}">
            <h3 style="margin:0 0 6px 0;">{analysis['status']}</h3>
            <p style="margin:0 0 8px 0; font-size: 0.95rem;"><strong>Motivo:</strong> {analysis['decision_label']} - {analysis['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)

        if analysis["recommendations"]:
            st.markdown("##### 📋 **Acciones Ejecutivas Recomendadas:**")
            for r in analysis["recommendations"]:
                st.write(f"• {r}")

# ==============================================================================
# TAB 5: IMPORTACIÓN & SOURCING DDP
# ==============================================================================
with tab_sourcing:
    st.markdown("### 🚢 **Importación & Fábricas: El Salto Dropshipping ➔ DDP**")
    st.caption("Modela la multiplicación del margen neto al importar lotes de 300 a 1,000 unidades y genera cartas de negociación RFQ en inglés para fábricas chinas.")

    sub_sc1, sub_sc2 = st.tabs([
        "📈 Comparador Económico (Dropship vs DDP)",
        "✉️ Generador de Mensajes RFQ (Alibaba / 1688)",
    ])

    with sub_sc1:
        c_sh1, c_sh2 = st.columns([1, 1.2])
        
        with c_sh1:
            st.markdown("#### ⚙️ **Parámetros del Producto & Lote**")
            sc_sale_price = st.number_input("Precio de Venta (PVP) [$]", value=float(eval_data["target_price"]) if eval_data else 39.99, min_value=1.0)
            sc_ds_cogs = st.number_input("Costo Unitario en Dropshipping [$]", value=float(eval_data["cost_unit"]) if eval_data else 9.50, min_value=0.5)
            sc_fob = st.number_input("Costo Unitario Fábrica FOB (300-1000 u.) [$]", value=3.20, min_value=0.1)
            sc_freight = st.number_input("Flete DDP Marítimo/Aéreo por Unidad [$]", value=1.80, min_value=0.1)
            sc_packaging = st.number_input("Empaque Private Label con Logo [$]", value=0.75, min_value=0.0)
            sc_3pl = st.number_input("Fulfillment / 3PL Local Pick & Pack [$]", value=3.20, min_value=0.0)
            sc_cpa = st.number_input("CPA Promedio de Pauta [$]", value=12.00, min_value=0.0)
            sc_units = st.select_slider("Tamaño del Lote de Importación (Unidades)", options=[100, 300, 500, 1000, 2000], value=500)

        with c_sh2:
            st.markdown("#### 📊 **Comparativa de Margen & Expansión de Ganancia**")
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

            c_mb1, c_mb2, c_mb3 = st.columns(3)
            c_mb1.metric("Margen Neto DS", f"${margin_data['dropship']['net_profit_unit']}", f"{margin_data['dropship']['net_margin_pct']}%")
            c_mb2.metric("Margen Neto DDP", f"${margin_data['bulk_ddp']['net_profit_unit']}", f"{margin_data['bulk_ddp']['net_margin_pct']}%")
            c_mb3.metric("Salto de Ganancia", f"+{margin_data['comparison']['profit_increase_pct']}%", f"+${margin_data['comparison']['extra_profit_unit']}/ud")

            st.markdown(f"""
            <div class="verdict-box-success" style="margin-top:16px;">
                <h3 style="margin:0 0 8px 0;">🚀 Impacto Financiero en Lote de {sc_units} Unidades</h3>
                <p style="margin:0 0 6px 0; font-size:1.05rem;">
                    • Ganancia Neta Total en Dropshipping: <strong>${margin_data['dropship']['batch_profit']:,.2f}</strong><br>
                    • Ganancia Neta Total con Importación DDP: <strong>${margin_data['bulk_ddp']['batch_profit']:,.2f}</strong><br>
                    • <strong>Beneficio Extra en el Bolsillo:</strong> <span style="font-size:1.2rem; color:#34d399;">+${margin_data['comparison']['extra_profit_batch']:,.2f} USD</span>
                </p>
                <hr style="border-color:rgba(255,255,255,0.2);">
                <p style="margin:0; font-size:0.9rem;">
                    📦 Capital Requerido para Producción: <strong>${margin_data['bulk_ddp']['capital_required']:,.2f}</strong> | Retorno sobre Inventario (ROI): <strong>{margin_data['bulk_ddp']['roi_inventory_pct']}%</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)

    with sub_sc2:
        st.markdown("#### ✉️ **Generador de RFQ Profesional en Inglés**")
        st.caption("Plantilla con terminología de comercio internacional (Incoterms, AQL 2.5, Private Label, Master Carton Specs).")

        c_rf1, c_rf2 = st.columns(2)
        with c_rf1:
            rfq_company = st.text_input("Nombre de tu Empresa / Marca", value="Apex Direct E-Commerce Group")
            rfq_name = st.text_input("Tu Nombre / Cargo", value="Alex Morgan, Head of Procurement")
            rfq_prod = st.text_input("Producto Específico a Cotizar", value=active_p.get("china_keywords", "Ergonomic Lumbar Support Back Cushion"))
        with c_rf2:
            rfq_dest = st.text_input("País y Almacén de Destino", value="United States (Florida 3PL Fulfillment Center)")
            rfq_logo = st.checkbox("Incluir Logo Personalizado (Laser / Silk)", value=True)
            rfq_box = st.checkbox("Incluir Caja Custom 4C con Inserto", value=True)
            rfq_barcode = st.checkbox("Incluir Código de Barras UPC y Tarjeta de Agradecimiento", value=True)

        rfq_output = SourcingHub.generate_rfq_message(
            company_name=rfq_company,
            contact_name=rfq_name,
            product_name=rfq_prod,
            target_destination_country=rfq_dest,
            custom_logo=rfq_logo,
            custom_box=rfq_box,
            barcode_labeling=rfq_barcode,
        )

        st.markdown("##### 📋 **Mensaje Listo para Copiar y Enviar por Chat de Alibaba / 1688:**")
        st.code(rfq_output, language="text")

# ==============================================================================
# TAB 6: MEMORIA & LECCIONES APRENDIDAS (BASE DE DATOS PERSISTENTE)
# ==============================================================================
with tab_db:
    st.markdown("### 🧠 **Memoria Operativa & Sistema de Aprendizaje Continuo**")
    st.caption("Almacén persistente en SQLite: Reglas de operadores de alto rendimiento e historial de validaciones.")

    sub_db1, sub_db2, sub_db3 = st.tabs([
        "📜 Reglas & Principios Operativos",
        "🗂️ Historial de Productos Validados",
        "➕ Agregar Nueva Regla / Aprendizaje",
    ])

    with sub_db1:
        rules = kb.get_all_rules()
        for r in rules:
            with st.expander(f"📌 **[{r['category']}] {r['title']}** — _{r['author']}_"):
                st.markdown(f"**Regla:** {r['rule']}")
                st.info(f"💡 **Consejo Accionable:** {r['actionable_tip']}")

    with sub_db2:
        products = kb.get_all_products()
        if not products:
            st.info("Aún no hay productos guardados en la base de datos. Evalúa uno en la pestaña de 'Radar & Validación' y haz clic en Guardar.")
        else:
            df_prods = pd.DataFrame(products)
            st.dataframe(
                df_prods[["id", "product_name", "category", "product_type", "multiplier", "total_score", "verdict", "status", "created_at"]],
                use_container_width=True,
            )

            st.markdown("---")
            st.markdown("#### ✏️ **Actualizar Estado o Lecciones Aprendidas**")
            col_u1, col_u2, col_u3 = st.columns([1, 1, 2])
            with col_u1:
                selected_id = st.selectbox("ID de Producto a Actualizar", [p["id"] for p in products])
            with col_u2:
                new_status = st.selectbox("Nuevo Estado", ["Evaluado", "En Testeo", "Escalado DDP", "Descartado"])
            with col_u3:
                new_lessons = st.text_input("Lección Aprendida del Testeo", value="Excelente CTR en TikTok, margen optimizado con bundle x2.")

            if st.button("Guardar Actualización"):
                kb.update_product_status(selected_id, new_status, new_lessons)
                st.success(f"Producto #{selected_id} actualizado.")
                st.rerun()

    with sub_db3:
        st.markdown("#### ➕ **Registrar Nueva Regla Operativa en la Base de Datos**")
        with st.form("new_rule_form"):
            r_author = st.text_input("Autor / Fuente", value="DTC Scale Framework")
            r_cat = st.selectbox("Categoría", ["Validation & Margin", "Creatives & Testing", "Pauta & Ads", "Sourcing & DDP", "General Strategy"])
            r_title = st.text_input("Título de la Regla", value="Velocidad de Despacho en Dropshipping")
            r_rule = st.text_area("Descripción de la Regla", value="Nunca trabajar con proveedores cuyo tiempo de procesamiento supere las 48 horas.")
            r_tip = st.text_input("Consejo Accionable", value="Exigir número de tracking de YunExpress o 4PX antes de escalar.")
            
            submitted = st.form_submit_button("Guardar Regla en Memoria")
            if submitted:
                kb.add_custom_rule(r_author, r_cat, r_title, r_rule, r_tip)
                st.success("¡Regla guardada permanentemente en la base de datos!")
                st.rerun()
