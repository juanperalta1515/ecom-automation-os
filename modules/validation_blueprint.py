"""
Validation Blueprint & Roadmap Generator Module
Generates an actionable step-by-step operational roadmap for testing via the optimal dropshipping platform, validating mass volume, and transitioning to bulk DDP factory sourcing.
"""

from typing import Dict, Any, List


class ValidationBlueprint:
    """
    Generates tailored execution blueprints for validated e-commerce products.
    """

    @staticmethod
    def generate_roadmap(
        product_name: str,
        category: str,
        product_type: str,
        cost_unit: float,
        target_price: float,
        target_cpa: float,
        target_market: str = "Estados Unidos / Global (Inglés)",
        fulfillment_mode: str = "Automático (Recomendado por Sistema)",
    ) -> Dict[str, Any]:
        """
        Builds a 3-phase execution roadmap from initial dropshipping test to bulk DDP private label import.
        """
        multiplier = round(target_price / max(0.01, cost_unit), 2)
        daily_test_budget = round(target_cpa * 3.0, 2)  # 3X Target CPA
        max_stop_loss_spend = round(target_cpa * 1.0, 2)
        target_orders_validation = 35  # Target milestone: 35-50 orders in 7 days

        # Select Optimal Dropshipping Platform
        recommended_platform = ""
        platform_reason = ""
        integration_app = ""

        if "LATAM" in target_market or "Contraentrega" in target_market:
            recommended_platform = "Dropi / Hoko / 99Minutos (Modelo Pago Contraentrega / COD)"
            platform_reason = "En mercados hispanos y LATAM, el modelo COD (Cash On Delivery) convierte 3x a 5x más que las pasarelas tradicionales con stock local en bodega."
            integration_app = "Shopify + Dropi App / Releasit COD Form"
        elif "TikTok" in category or product_type == "Viral/Trend":
            recommended_platform = "CJ Dropshipping / Zendrop (Líneas Rápidas US/EU 6-9 Días)"
            platform_reason = "Productos de tendencia visual requieren sincronización de inventario en tiempo real y tiempos de despacho con tracking en menos de 48h para evitar contracargos."
            integration_app = "Shopify + CJ Dropshipping Sync / Zendrop Pro"
        else:  # Evergreen
            recommended_platform = "CJ Dropshipping / Wiio / Agente Privado de Sourcing"
            platform_reason = "Permite solicitar empaque neutro sin publicidad de AliExpress y mejor control de calidad por lote para productos de uso diario continuo."
            integration_app = "Shopify + DSers / CJ Dropshipping"

        phases = [
            {
                "phase_number": "FASE 1",
                "phase_title": "Configuración de la Oferta Mínima Viable (MVP) & Plataforma Dropshipping",
                "badge": "Día 1 - 2",
                "steps": [
                    {
                        "step_title": "1.1 Conexión con Proveedor de Dropshipping",
                        "details": f"Importar el producto **{product_name}** a tu tienda utilizando **{recommended_platform}**. Verificar que el costo base más envío ePacket/YunExpress no supere **${cost_unit:.2f} USD**.",
                        "tip": "Solicitar al agente de la plataforma que confirme stock disponible mayor a 500 unidades antes de encender pauta."
                    },
                    {
                        "step_title": "1.2 Arquitectura de Conversión en Shopify",
                        "details": f"Publicar la ficha de producto con el título optimizado, viñetas de dolor/solución (PAS) y configurar los 3 bundles de checkout: 1 unidad a **${target_price:.2f}**, 2 unidades con 15% OFF (**${(target_price*0.85*2):.2f}**) y 3 unidades con 25% OFF + Envío Gratis (**${(target_price*0.75*3):.2f}**).",
                        "tip": "Instalar aplicación de Bundles / Upsell (como Kaching Bundles o Wide Bundles) para forzar un AOV (Ticket Promedio) más alto."
                    },
                    {
                        "step_title": "1.3 Pasarela de Pago & Políticas Blindadas",
                        "details": "Asegurar pasarela activa (Stripe / Shopify Payments / PayPal / COD Form) y publicar páginas legales (Política de Envíos de 7-12 días, Garantía de Devolución de 30 Días y Contacto de Soporte).",
                        "tip": "Tener configurado el correo de confirmación de pedido con número de seguimiento para reducir disputas al 0%."
                    }
                ]
            },
            {
                "phase_number": "FASE 2",
                "phase_title": "Protocolo de Testeo de Tráfico & Validación de Volumen",
                "badge": "Día 3 - 9",
                "steps": [
                    {
                        "step_title": "2.1 Lanzamiento de Campaña Dinámica 3:2:2",
                        "details": f"Crear 1 Campaña de Prueba (CBO o ABO) en Meta Ads con **3 Hooks de video distintos (0-3s)**, **2 Cuerpos demostrativos** y **2 Textos principales**. Presupuesto diario asignado: **${daily_test_budget:.2f} USD/día** (3X CPA Objetivo).",
                        "tip": "Público amplio (Broad) o 3-5 intereses consolidados del nicho. Dejar que el algoritmo encuentre los compradores."
                    },
                    {
                        "step_title": "2.2 Regla de Corte Implacable (Stop-Loss)",
                        "details": f"Si un creativo gasta **${max_stop_loss_spend:.2f} USD** (1X CPA Objetivo) sin ninguna compra, se apaga antes de medianoche. Si gasta el 50% del CPA sin ningún 'Add to Cart', descartar el ángulo de creativo.",
                        "tip": "Cero emoción en la toma de decisiones: cortar pérdidas rápido y redirigir presupuesto al hook con mejor CTR (>1.5%)."
                    },
                    {
                        "step_title": "2.3 Hito de Validación de Masa Crítica",
                        "details": f"**Criterio de Validación Exitosa:** Lograr entre **{target_orders_validation} y 50 pedidos** en los primeros 7 días con un ROAS estable sobre el Break-Even.",
                        "tip": "En cuanto se alcance este hito, el producto queda oficialmente VALIDADO como ganador de mercado."
                    }
                ]
            },
            {
                "phase_number": "FASE 3",
                "phase_title": "Transición a Importación DDP & Escalamiento a Gran Escala",
                "badge": "Día 10 en Adelante",
                "steps": [
                    {
                        "step_title": "3.1 Cotización con Fabricantes Directos en China (1688 / Alibaba)",
                        "details": f"Enviar el mensaje **RFQ profesional generado por el sistema** a 3-5 fábricas verificadas (Gold Suppliers / Verified Manufacturers). Solicitar precios escalonados (300, 500 y 1,000 unidades) bajo términos **Incoterms DDP** (flete marítimo y aéreo con impuestos aduaneros pagos en destino).",
                        "tip": "Negociar siempre el empaque personalizado con logo (Private Label) y pedir tarjeta de inserto de agradecimiento para construir marca."
                    },
                    {
                        "step_title": "3.2 Pedido de Muestra & Control de Calidad (AQL 2.5)",
                        "details": "Pedir 1-2 unidades de muestra por DHL/FedEx Express para verificar acabado, costuras o componentes electrónicos. Contratar inspección de calidad previa al embarque.",
                        "tip": "Pagar el 30% de anticipo para iniciar producción y el 70% restante únicamente tras recibir el reporte de inspección aprobado."
                    },
                    {
                        "step_title": "3.3 Traspaso a Almacén 3PL Local & Campaña Advantage+ (ASC)",
                        "details": "Recibir el lote consolidado en tu centro de fulfillment 3PL local (envíos en 24-48h a tus clientes). Traspasar los creativos ganadores a campañas **Meta Advantage+ Shopping (ASC)** para escalar el presupuesto diario un 20% cada 48h con un margen neto duplicado (>35-45%).",
                        "tip": "Con stock local y envíos de 24-48h, las reseñas suben a 4.9 estrellas y la tasa de recompra se multiplica."
                    }
                ]
            }
        ]

        return {
            "product_name": product_name,
            "category": category,
            "target_market": target_market,
            "recommended_platform": recommended_platform,
            "platform_reason": platform_reason,
            "integration_app": integration_app,
            "daily_test_budget": daily_test_budget,
            "max_stop_loss_spend": max_stop_loss_spend,
            "target_orders_validation": target_orders_validation,
            "phases": phases,
        }
