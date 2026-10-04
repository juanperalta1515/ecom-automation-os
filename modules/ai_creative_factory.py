"""
AI Creative Factory Module
Generates Meta Ads 3:2:2 video scripts, Shopify PAS/AIDA product listings, bundle offers, and ready-to-use ElevenLabs & Midjourney/Flair.ai prompts.
"""

from typing import Dict, Any, List


class AICreativeFactory:
    """
    Automates creative generation for Meta Ads testing and Shopify conversion rate optimization (CRO).
    """

    @staticmethod
    def generate_meta_322_scripts(
        product_name: str,
        category: str,
        target_audience: str,
        core_pain: str,
        main_benefit: str,
        target_price: float,
    ) -> Dict[str, Any]:
        """
        Generates 3 distinct hooks + 2 body variations + 2 CTAs according to Meta's 3:2:2 dynamic testing framework.
        """
        price_str = f"${target_price:.2f}"

        # 3 Distinct Hooks (0 - 3 seconds)
        hooks = [
            {
                "id": "Hook 1 (Shock / Curiosidad)",
                "visual_action": f"[Primer plano rápido a cámara con corte abrupto]: La persona sostiene el {product_name} con expresión de sorpresa o muestra el error común de la competencia.",
                "voiceover_es": f"¡Si todavía estás luchando con {core_pain}, necesitas dejar lo que estás haciendo y mirar esto!",
                "on_screen_text": f"🚨 ¿Aún sufres por {core_pain[:30]}...? Mira esto 👇",
            },
            {
                "id": "Hook 2 (Dolor Directo / Empatía Aguda)",
                "visual_action": f"[Toma cotidiana en primer plano]: Persona frustrada sufriendo exactamente por {core_pain}. Cambio súbito a blanco y negro con efecto de estrés.",
                "voiceover_es": f"El 90% de las personas comete este error intentando resolver {core_pain} sin saber que hay una forma 10 veces más rápida.",
                "on_screen_text": f"❌ Deja de perder tiempo con {core_pain[:28]}...",
            },
            {
                "id": "Hook 3 (Demostración de Transformación Rápida)",
                "visual_action": f"[Pantalla dividida Antes / Después de 1.5 segundos]: A la izquierda el problema caótico, a la derecha el {product_name} resolviéndolo en 2 segundos.",
                "voiceover_es": f"Probé decenas de soluciones para {core_pain}... y este pequeño dispositivo cambió todo en 48 horas.",
                "on_screen_text": f"✨ El cambio de 0 a 100 con {product_name} 🔥",
            },
        ]

        # 2 Body / Demonstration Variations (3 - 20 seconds)
        bodies = [
            {
                "id": "Variación A (Fórmula PAS - Problema, Agitación, Mecanismo)",
                "visual_flow": f"1. Demostración en uso real del {product_name} en ángulo de 45°.\n2. Zoom a los detalles de calidad o función clave.\n3. Reacción de alivio genuino y sonrisa de satisfacción.",
                "voiceover_es": f"El problema es que las soluciones tradicionales son caras y lentas. El nuevo {product_name} fue diseñado específicamente para {main_benefit} sin complicaciones. Simplemente lo usas y sientes la diferencia desde el minuto uno.",
            },
            {
                "id": "Variación B (Fórmula AIDA - Interés, Deseo, Prueba Social)",
                "visual_flow": f"1. Unboxing express o puesta en marcha instantánea.\n2. Superposición de 5 estrellas ★★★★★ y citas de reseñas de clientes felices.\n3. Demostración de portabilidad o practicidad extrema.",
                "voiceover_es": f"Diseñado con tecnología de grado premium, te permite conseguir {main_benefit} en segundos. Miles de personas en todo el país ya lo convirtieron en su accesorio esencial de todos los días.",
            },
        ]

        # 2 Call To Action Variations (Últimos 5 segundos)
        ctas = [
            {
                "id": "CTA 1 (Urgencia & Descuento de Lanzamiento)",
                "visual_flow": f"Mockup del producto en caja + Sticker '50% OFF HOY' + botón animado de 'Comprar Ahora'.",
                "voiceover_es": f"Haz clic en el enlace de abajo y aprovecha el 50% de descuento con envío express antes de que se agote el stock de lanzamiento.",
                "on_screen_text": f"🔥 50% OFF SOLO POR HOY | Envío Rápido 🚚",
            },
            {
                "id": "CTA 2 (Garantía de Satisfacción 100% Cero Riesgo)",
                "visual_flow": f"Insignia de 'Garantía de 30 Días' + Botón parpadeante 'Pide el tuyo aquí'.",
                "voiceover_es": f"Pruébalo durante 30 días sin riesgo. Si no transforma tu día, te devolvemos el 100% de tu dinero. Toca 'Comprar Ahora'.",
                "on_screen_text": f"🛡️ Garantía de Devolución de 30 Días | Stock Limitado",
            },
        ]

        return {
            "framework": "Meta Ads 3:2:2 Testing Engine",
            "product_name": product_name,
            "target_price": price_str,
            "hooks": hooks,
            "bodies": bodies,
            "ctas": ctas,
        }

    @staticmethod
    def generate_shopify_listing(
        product_name: str,
        category: str,
        target_audience: str,
        core_pain: str,
        main_benefit: str,
        target_price: float,
    ) -> Dict[str, Any]:
        """
        Generates high-converting Shopify product descriptions, PAS/AIDA bullet points, and high-AOV bundle tables.
        """
        p1 = target_price
        p2_unit = round(target_price * 0.85, 2)  # 15% discount
        p2_total = round(p2_unit * 2, 2)
        p3_unit = round(target_price * 0.75, 2)  # 25% discount
        p3_total = round(p3_unit * 3, 2)

        seo_title = f"{product_name} Pro™ - Solución Premium para {main_benefit.title()} | Envío Express"

        bullets_pas = [
            f"⚡ **Adiós a {core_pain}:** Diseñado ergonómicamente para atacar el origen del problema de raíz sin esfuerzo.",
            f"🎯 **{main_benefit.capitalize()}:** Obtén resultados tangibles y medibles desde el primer uso comprobado.",
            f"💎 **Materiales de Calidad Grado Profesional:** Construcción ultra resistente y duradera para uso diario continuo.",
            f"🚀 **Ahorro de Tiempo y Dinero:** Olvídate de costosos tratamientos o productos genéricos que no funcionan.",
            f"🛡️ **Garantía Blindada de 30 Días:** Si no cumple 100% tus expectativas, te devolvemos el dinero sin preguntas.",
        ]

        bundles = [
            {
                "tier": "Paquete 1 Unidad",
                "badge": "Prueba Individual",
                "price": f"${p1:.2f}",
                "savings": "Precio Regular",
                "shipping": "Envío Estándar",
            },
            {
                "tier": "Paquete 2 Unidades (Dúo Pack)",
                "badge": "🔥 MÁS POPULAR (Ahorra 15%)",
                "price": f"${p2_total:.2f} (${p2_unit:.2f}/ud)",
                "savings": f"Ahorras ${(p1 * 2 - p2_total):.2f}",
                "shipping": "Envío Prioritario Bonificado",
            },
            {
                "tier": "Paquete 3 Unidades (Familiar / Regalo)",
                "badge": "⭐ MEJOR VALOR (Ahorra 25%)",
                "price": f"${p3_total:.2f} (${p3_unit:.2f}/ud)",
                "savings": f"Ahorras ${(p1 * 3 - p3_total):.2f}",
                "shipping": "Envío Express GRATIS a Todo el País",
            },
        ]

        faqs = [
            {
                "q": "¿En cuánto tiempo recibiré mi pedido?",
                "a": "Los envíos se despachan dentro de las 24-48 horas hábiles con número de seguimiento en tiempo real.",
            },
            {
                "q": "¿Qué pasa si no me convence el producto?",
                "a": "Ofrecemos garantía de satisfacción de 30 días. Si no estás fascinado con los resultados, te reembolsamos tu compra.",
            },
            {
                "q": "¿Es seguro comprar en este sitio web?",
                "a": "Procesamos pagos mediante pasarelas con cifrado SSL de 256 bits y protección total al comprador.",
            },
        ]

        return {
            "seo_title": seo_title,
            "bullets": bullets_pas,
            "bundles": bundles,
            "faqs": faqs,
        }

    @staticmethod
    def generate_ai_prompts(product_name: str, category: str, main_benefit: str) -> Dict[str, str]:
        """
        Generates copy-paste ready prompts for ElevenLabs and Midjourney / Flair.ai.
        """
        elevenlabs_prompt = (
            f"Voice Style: Engaging, energetic yet authoritative, warm commercial American or Latin-Spanish tone. "
            f"Pacing: 1.1x speed for TikTok / Meta Reels. Emotional arc: starts curious/concerned, shifts to enthusiastic, "
            f"ends with high urgency CTA. Stability: 0.45, Clarity: 0.85, Style Exaggeration: 0.20."
        )

        midjourney_prompt = (
            f"/imagine prompt: Commercial studio hero photography of a modern sleek {product_name} in {category} niche, "
            f"clean minimalist luxury background, soft studio rim lighting, subtle pastel aesthetic, depth of field, "
            f"ultra sharp focus, shot on Hasselblad H6D-100c, 8k resolution, photorealistic, advertising mockup style --ar 1:1 --v 6.0 --style raw"
        )

        flair_ai_prompt = (
            f"Product: {product_name}. Background scene: Elegant wooden marble podium surrounded by subtle aesthetic props related to {category}. "
            f"Natural window sunlight streaming from the left, soft shadows, high-end e-commerce DTC brand look."
        )

        return {
            "elevenlabs": elevenlabs_prompt,
            "midjourney": midjourney_prompt,
            "flair_ai": flair_ai_prompt,
        }
