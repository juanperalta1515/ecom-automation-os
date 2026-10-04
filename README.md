# ⚡ E-Commerce Automation OS (`ecom-automation-os`)

Sistema integral y modular de automatización para la **validación ágil de productos**, **generación de creativos con IA**, **control algorítmico de pauta publicitaria** y **escalamiento a gran escala mediante importación DDP** (inspirado en la metodología de referencia de operadores de alto rendimiento como Mauro Stendel).

---

## 🎯 Enfoque de Nicho del Sistema

El motor está calibrado especialmente para:
1. **Productos Virales con Alto Tráfico (Trend-Driven):** Artículos con efecto "WOW" visual inmediato para TikTok y Meta Ads (scroll-stoppers de 0 a 3 segundos).
2. **Productos Perennes (Evergreen):** Soluciones de alta demanda que se venden los 12 meses del año sin estacionalidad (Salud/Postura, Gadgets de cocina/hogar, Organización, Estética/Cuidado personal y Accesorios ergonómicos).

---

## 🏗️ Arquitectura del Proyecto

```
ecom-automation-os/
├── app.py                      # Dashboard ejecutivo en Streamlit con UI moderna Dark Mode
├── requirements.txt            # Dependencias del proyecto (streamlit, pandas, requests, etc.)
├── .env.example                # Variables de entorno y configuración
├── .gitignore                  # Exclusiones de Git estándar
├── README.md                   # Documentación técnica y operacional
├── modules/
│   ├── __init__.py
│   ├── product_radar.py        # Motor de scoring de la "Regla de los 5 Pilares"
│   ├── ai_creative_factory.py  # Generador de guiones 3:2:2, fichas Shopify y prompts IA
│   ├── ads_analytics.py        # Calculadora de Break-Even ROAS y motor Kill/Scale
│   ├── sourcing_hub.py         # Calculador de salto de margen y generador de RFQ en inglés
│   └── knowledge_base.py       # Almacén de persistencia SQLite y reglas operativas
└── data/
    ├── rules.json              # Reglas doradas pre-cargadas (Mauro Stendel, Meta Ads, etc.)
    └── ecom_data.db            # Base de datos SQLite local autogenerada
```

---

## 🧩 Módulos Principales

### 1. 🎯 `product_radar.py` — Radar de los 5 Pilares
Calcula un índice de viabilidad sobre 100 puntos evaluando:
- **Margen Mínimo 3X-5X:** Relación directa PVP vs. Costo Unitario en origen.
- **Estacionalidad:** Calibración Evergreen (12 meses continuos) vs. Viral/Trend.
- **Efecto WOW (0-3s) y Nivel de Dolor:** Capacidad de detención de scroll y agitación de problemas reales.
- **Escasez Offline:** Dificultad para encontrar el artículo en comercios físicos convencionales.
- **Seguridad Logística:** Filtro contra productos con talles complejos (textil), fragilidad (vidrio) o peso excesivo.
- **Semáforo:** Emite veredicto en tiempo real (🟢 *Aprobado para Testeo*, 🟡 *Dudoso / Requiere Ajuste*, 🔴 *Descartado*).

### 2. 🎨 `ai_creative_factory.py` — Fábrica de Creativos
- **Método 3:2:2 de Meta Ads:** 3 Hooks visuales diferentes (0-3s), 2 variaciones de cuerpo/demostración (fórmulas PAS y AIDA) y 2 Call-to-Actions con escasez y garantía.
- **Shopify CRO & Bundles:** Títulos SEO optimizados, viñetas emocionales y ofertas escalonadas (x1, x2 con 15% OFF, x3 con 25% OFF + Envío Gratis).
- **Prompt Matrix:** Prompts listos para copiar en **ElevenLabs** (locución profesional) y **Midjourney v6 / Flair.ai** (fotografía publicitaria hiperrealista).

### 3. 📊 `ads_analytics.py` — Control de Pauta & Algoritmo Kill/Scale
- **Guardarraíles Financieros:** Cálculo automático de **Break-Even ROAS** y **CPA Objetivo** según el margen neto deseado.
- **Decisión Algorítmica Implacable:**
  - 🔴 **KILL:** Apaga anuncios si el gasto supera 1.0X CPA Objetivo sin ventas o 0.5X CPA Objetivo sin ningún *Add to Cart*.
  - 🟡 **HOLD:** Mantiene en fase de aprendizaje mientras se evalúan los primeros datos.
  - 🟢 **ESCALAR (+20%):** Aumentos diarios controlados de presupuesto.
  - 🚀 **ESCALAR A ADVANTAGE+ (ASC):** Transición automática a campañas ASC cuando el ROAS es $\ge 2.2x$ de forma estable.

### 4. 🚢 `sourcing_hub.py` — Importación & Sourcing DDP
- **Simulador de Margen:** Modela el salto de rentabilidad unitaria y en lote (300 a 1,000 unidades) pasando de Dropshipping tradicional a Importación DDP con empaque Private Label y fulfillment 3PL local.
- **Generador de RFQ en Inglés:** Mensaje formal de solicitud de cotización con estándares internacionales (Incoterms DDP, control AQL 2.5, especificaciones de master carton y personalización).

### 5. 🧠 `knowledge_base.py` — Memoria Persistente & Aprendizaje Continuo
- Base de datos SQLite para registrar todas las validaciones de productos.
- Registro de lecciones aprendidas por campaña.
- Repositorio de reglas operativas de referentes del sector.

---

## 🚀 Instalación y Puesta en Marcha

### Prerrequisitos
- Python 3.9 o superior.

### 1. Clonar o navegar al directorio:
```bash
cd ecom-automation-os
```

### 2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación:
```bash
streamlit run app.py
```

El panel interactivo se abrirá automáticamente en tu navegador web en `http://localhost:8501`.

---

## 🛡️ Licencia y Uso
Diseñado para operadores de e-commerce, media buyers e importadores. Código modular y extensible.
