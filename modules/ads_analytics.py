"""
Ads Analytics & Media Buying Optimization Module
Calculates Break-Even ROAS, Target CPA, and algorithmic Kill / Scale decision matrices for Meta Ads & TikTok Ads.
"""

from typing import Dict, Any, List


class AdsAnalytics:
    """
    Algorithmic Media Buying Assistant.
    """

    @staticmethod
    def calculate_targets(
        sale_price: float,
        cost_unit: float,
        shipping_fee_charged: float = 0.0,
        gateway_fee_pct: float = 3.5,  # Shopify Payments / Stripe / PayPal
        desired_net_margin_pct: float = 25.0,  # 25% target profit after ads
    ) -> Dict[str, Any]:
        """
        Computes key financial guardrails: Break-Even ROAS and Target CPA.
        """
        total_revenue = sale_price + shipping_fee_charged
        gateway_fee = total_revenue * (gateway_fee_pct / 100.0)
        cogs_and_fees = cost_unit + gateway_fee
        gross_profit = total_revenue - cogs_and_fees

        gross_margin_pct = (gross_profit / total_revenue) * 100.0 if total_revenue > 0 else 0.0

        # Break-even ROAS = 1 / Gross Margin %
        be_roas = (100.0 / gross_margin_pct) if gross_margin_pct > 0 else 999.0
        be_cpa = gross_profit  # Break-even CPA is the entire gross profit

        # Target CPA to achieve desired net profit margin
        desired_net_profit = total_revenue * (desired_net_margin_pct / 100.0)
        target_cpa = max(1.0, gross_profit - desired_net_profit)
        target_roas = total_revenue / target_cpa if target_cpa > 0 else be_roas

        return {
            "sale_price": sale_price,
            "cost_unit": cost_unit,
            "total_revenue": round(total_revenue, 2),
            "gross_profit": round(gross_profit, 2),
            "gross_margin_pct": round(gross_margin_pct, 1),
            "be_roas": round(be_roas, 2),
            "be_cpa": round(be_cpa, 2),
            "target_cpa": round(target_cpa, 2),
            "target_roas": round(target_roas, 2),
            "desired_net_profit_per_order": round(desired_net_profit, 2),
        }

    @staticmethod
    def analyze_ad_performance(
        ad_name: str,
        spend: float,
        impressions: int,
        link_clicks: int,
        add_to_carts: int,
        purchases: int,
        revenue: float,
        target_cpa: float,
        be_roas: float,
    ) -> Dict[str, Any]:
        """
        Applies algorithmic stop-loss and scaling rules.
        """
        spend = max(0.0, float(spend))
        impressions = max(1, int(impressions))
        link_clicks = max(0, int(link_clicks))
        add_to_carts = max(0, int(add_to_carts))
        purchases = max(0, int(purchases))
        revenue = max(0.0, float(revenue))

        # Core Metrics
        cpm = round((spend / impressions) * 1000.0, 2)
        ctr_link = round((link_clicks / impressions) * 100.0, 2)
        cpc = round(spend / link_clicks, 2) if link_clicks > 0 else 0.0
        real_cpa = round(spend / purchases, 2) if purchases > 0 else 0.0
        real_roas = round(revenue / spend, 2) if spend > 0 else 0.0

        # Algorithmic Evaluation
        status = ""
        action_color = ""
        decision_label = ""
        explanation = ""
        recommendations: List[str] = []

        # Rule 1: No Sales and High Spend (Kill Condition)
        if purchases == 0:
            if spend >= target_cpa:
                status = "🔴 KILL (APAGAR INMEDIATAMENTE)"
                action_color = "error"
                decision_label = "Corte de Sangría (Stop-Loss)"
                explanation = f"El anuncio gastó ${spend:.2f} (>= 1.0X CPA Objetivo ${target_cpa:.2f}) con 0 compras registradas."
                recommendations.append("Apagar el conjunto de anuncios/creativo para no quemar presupuesto en tráfico frío sin intención.")
            elif spend >= (target_cpa * 0.5) and add_to_carts == 0:
                status = "🔴 KILL (APAGAR)"
                action_color = "error"
                decision_label = "Falta Total de Intención de Compra"
                explanation = f"Gastó ${spend:.2f} (50% del CPA Objetivo) sin generar un solo 'Add to Cart'."
                recommendations.append("El gancho o la oferta no resuenan con la audiencia. Reemplazar creativo o mejorar pricing.")
            else:
                status = "🟡 TESTING (EN OBSERVACIÓN)"
                action_color = "warning"
                decision_label = "Fase de Aprendizaje Temprano"
                explanation = f"Gasto actual (${spend:.2f}) aún por debajo del umbral de stop-loss (${target_cpa:.2f})."
                recommendations.append(f"Dejar correr hasta alcanzar ${target_cpa:.2f} de gasto antes de tomar una decisión definitiva.")

        # Rule 2: Sales with Underperforming ROAS (Kill / Optimize)
        elif real_roas < be_roas:
            status = "🔴 KILL / REESTRUCTURAR"
            action_color = "error"
            decision_label = "ROAS No Rentable (Por debajo del Punto de Equilibrio)"
            explanation = f"ROAS real de {real_roas:.2f}x es menor al Break-Even ({be_roas:.2f}x). Cada venta genera pérdida neta."
            recommendations.append("Revisar si el CTR es bajo (<1.0%) o si la página de aterrizaje tiene baja tasa de conversión.")
            recommendations.append("Intentar bundle de 2x/3x unidades en la tienda para subir el Ticket Promedio antes de re-testear.")

        # Rule 3: Profitable and Stable (Scale to ASC)
        elif real_roas >= (be_roas * 1.4) and real_cpa <= target_cpa:
            if real_roas >= 2.2 and purchases >= 5:
                status = "🚀 ESCALAR A ADVANTAGE+ (ASC)"
                action_color = "success"
                decision_label = "Creativo Ganador Validado"
                explanation = f"ROAS excepcional de {real_roas:.2f}x (CPA: ${real_cpa:.2f} vs Objetivo: ${target_cpa:.2f}) con {purchases} ventas."
                recommendations.append("Transferir este ID de anuncio/post a una campaña Advantage+ Shopping (ASC).")
                recommendations.append("Asignar presupuesto inicial de 5X a 10X CPA Objetivo diario y escalar 20% cada 48h.")
            else:
                status = "🟢 ESCALAR VERTICAL (+20%)"
                action_color = "success"
                decision_label = "Rendimiento Rentable"
                explanation = f"ROAS de {real_roas:.2f}x por encima del Break-Even con CPA saludable."
                recommendations.append("Aumentar presupuesto diario un 20% para no reiniciar la fase de aprendizaje de Meta.")
        else:
            status = "🟡 MANTENER / HOLD"
            action_color = "info"
            decision_label = "Margen Aceptable en Observación"
            explanation = f"ROAS de {real_roas:.2f}x supera ligeramente el Break-Even ({be_roas:.2f}x), pero no alcanza el umbral de escala agresiva."
            recommendations.append("Mantener presupuesto constante y monitorear frecuencia de anuncios para evitar fatiga creativa.")

        # Secondary Creative Diagnostics
        if ctr_link < 1.0 and impressions > 1000:
            recommendations.append(f"⚠️ CTR de Enlace bajo ({ctr_link}%). Los primeros 3 segundos (Hooks) deben ser más llamativos.")
        elif ctr_link >= 2.0:
            recommendations.append(f"🔥 CTR de Enlace sobresaliente ({ctr_link}%). El creativo tiene excelente poder de retención.")

        return {
            "ad_name": ad_name,
            "spend": spend,
            "revenue": revenue,
            "purchases": purchases,
            "cpm": cpm,
            "cpc": cpc,
            "ctr_link": ctr_link,
            "real_cpa": real_cpa,
            "real_roas": real_roas,
            "be_roas": be_roas,
            "target_cpa": target_cpa,
            "status": status,
            "action_color": action_color,
            "decision_label": decision_label,
            "explanation": explanation,
            "recommendations": recommendations,
        }
