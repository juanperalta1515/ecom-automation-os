"""
Product Radar & Scoring Engine (5 Pillars Rule)
Evaluates e-commerce products with algorithmic scoring based on high-performance DTC methodology and top dropshipping/importing criteria.
"""

from typing import Dict, Any, List, Tuple


class ProductRadar:
    """
    Evaluates e-commerce products based on the 5 Pillars:
    1. Multiplier / Gross Margin (3X - 5X)
    2. Seasonality & Longevity (Evergreen vs Trend)
    3. Visual WOW Factor (0-3s) & Pain/Passion intensity
    4. Offline Scarcity (Hard to find locally)
    5. Logistical Feasibility & Low Return Risk
    """

    @staticmethod
    def evaluate_product(
        product_name: str,
        category: str,
        product_type: str,  # 'Viral/Trend' or 'Evergreen'
        cost_unit: float,
        target_price: float,
        wow_factor_score: int,  # 1 to 10
        pain_passion_score: int,  # 1 to 10
        offline_scarcity_score: int,  # 1 to 10
        has_size_variants: bool,  # True if fashion/apparel with complex sizes
        is_fragile: bool,  # Glass, high breakage risk
        is_heavy_or_bulky: bool,  # > 1.5 kg or bulky
        is_electric_or_battery_risk: bool,  # uncertified electronics
    ) -> Dict[str, Any]:
        """
        Calculates 100-point index and returns a comprehensive evaluation verdict.
        """
        cost_unit = max(0.01, float(cost_unit))
        target_price = max(0.01, float(target_price))
        multiplier = round(target_price / cost_unit, 2)
        gross_margin_pct = round(((target_price - cost_unit) / target_price) * 100, 1)

        # Pillar 1: Margin & Multiplier (Weight: 30 pts)
        # Target: >= 3.0x (base), >= 4.0x (optimal), >= 5.0x (max)
        margin_score = 0
        if multiplier >= 5.0:
            margin_score = 30
        elif multiplier >= 4.0:
            margin_score = 27
        elif multiplier >= 3.0:
            margin_score = 22
        elif multiplier >= 2.5:
            margin_score = 14
        elif multiplier >= 2.0:
            margin_score = 6
        else:
            margin_score = 0

        # Pillar 2: Seasonality & Longevity (Weight: 15 pts)
        seasonality_score = 0
        if product_type == "Evergreen":
            seasonality_score = 15  # Sells 12 months, continuous LTV
        else:  # Viral / Trend
            seasonality_score = 11  # Fast burst, shorter product lifecycle

        # Pillar 3: Visual WOW (0-3s) & Pain/Passion (Weight: 25 pts)
        # Normalizes 1-10 scores: (wow * 1.5) + (pain * 1.0) = max 25
        wow_norm = min(10, max(1, wow_factor_score))
        pain_norm = min(10, max(1, pain_passion_score))
        wow_pain_score = int(round((wow_norm * 1.3) + (pain_norm * 1.2)))
        wow_pain_score = min(25, wow_pain_score)

        # Pillar 4: Offline Scarcity (Weight: 15 pts)
        scarcity_norm = min(10, max(1, offline_scarcity_score))
        scarcity_score = int(round((scarcity_norm / 10.0) * 15))

        # Pillar 5: Logistical Risk & Return Feasibility (Weight: 15 pts)
        logistic_deductions = 0
        red_flags: List[str] = []

        if has_size_variants:
            logistic_deductions += 6
            red_flags.append("Riesgo de devoluciones por talles (Indumentaria/Calzado).")
        if is_fragile:
            logistic_deductions += 5
            red_flags.append("Producto frágil/cristal (Riesgo alto de rotura en flete).")
        if is_heavy_or_bulky:
            logistic_deductions += 3
            red_flags.append("Volumétrico/Pesado (>1.5kg): Flete DDP o ePacket costoso.")
        if is_electric_or_battery_risk:
            logistic_deductions += 3
            red_flags.append("Electrónica no homologada o baterías sin certificación MSDS.")

        logistic_score = max(0, 15 - logistic_deductions)

        # Total Calculation
        total_score = margin_score + seasonality_score + wow_pain_score + scarcity_score + logistic_score
        total_score = min(100, max(0, total_score))

        # Strengths & Highlights
        strengths: List[str] = []
        if multiplier >= 3.5:
            strengths.append(f"Excelente margen bruto ({multiplier}X / {gross_margin_pct}% de margen).")
        if wow_norm >= 8:
            strengths.append("Alto gancho visual en los primeros 3s (Ideal para TikTok/Reels).")
        if pain_norm >= 8:
            strengths.append("Resuelve un dolor claro y agudo o pasión intensa del comprador.")
        if product_type == "Evergreen":
            strengths.append("Demanda continua todo el año sin riesgo de colapso de tendencia.")
        if logistic_score == 15:
            strengths.append("Logística limpia y liviana: Bajo índice estimado de disputas y devoluciones.")

        # Verdict Decision Semaphore
        verdict = ""
        verdict_color = ""
        verdict_summary = ""
        action_recommendation = ""

        if multiplier < 2.5:
            verdict = "🔴 DESCARTADO"
            verdict_color = "error"
            verdict_summary = f"Multiplicador insuficiente ({multiplier}X). No absorberá el CPA de Meta ni comisiones de pasarela."
            action_recommendation = "Descartar o renegociar con el proveedor a un costo 40% menor antes de invertir en pauta."
        elif total_score >= 78 and len(red_flags) == 0 and multiplier >= 3.0:
            verdict = "🟢 APROBADO PARA TESTEO"
            verdict_color = "success"
            verdict_summary = f"Puntaje sobresaliente ({total_score}/100). Cumple los 5 pilares operativos con amplio colchón financiero."
            action_recommendation = "Lanzar campaña de validación con estructura 3:2:2 en Meta Ads. Presupuesto diario inicial sugerido: 3X CPA Objetivo ($45-$60/día)."
        elif total_score >= 60:
            verdict = "🟡 DUDOSO / REQUIERE AJUSTE"
            verdict_color = "warning"
            verdict_summary = f"Puntaje moderado ({total_score}/100). Viable únicamente si se corrigen los puntos débiles detectados."
            action_recommendation = "Crear ofertas Bundle (Lleva 2 con 15% OFF / Lleva 3 con 25% OFF) para elevar el AOV (Ticket Promedio) y mitigar el riesgo logístico."
        else:
            verdict = "🔴 DESCARTADO"
            verdict_color = "error"
            verdict_summary = f"Puntaje bajo ({total_score}/100). Falla en pilares críticos (margen, diferenciación o riesgo logístico)."
            action_recommendation = "No invertir en creativos ni pauta. Buscar alternativas en el mismo nicho con mayor efecto WOW y menor fricción logística."

        return {
            "product_name": product_name,
            "category": category,
            "product_type": product_type,
            "cost_unit": cost_unit,
            "target_price": target_price,
            "multiplier": multiplier,
            "gross_margin_pct": gross_margin_pct,
            "total_score": total_score,
            "pillar_breakdown": {
                "Margen & Multiplicador (Max 30)": margin_score,
                "Estacionalidad & Longevidad (Max 15)": seasonality_score,
                "Efecto WOW & Dolor/Pasión (Max 25)": wow_pain_score,
                "Escasez en Tienda Física (Max 15)": scarcity_score,
                "Seguridad Logística (Max 15)": logistic_score,
            },
            "strengths": strengths,
            "red_flags": red_flags,
            "verdict": verdict,
            "verdict_color": verdict_color,
            "verdict_summary": verdict_summary,
            "action_recommendation": action_recommendation,
        }
