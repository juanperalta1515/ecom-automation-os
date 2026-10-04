"""
Product Catalog & Intelligent Finder Module
Curated database of pre-researched high-potential e-commerce products (Evergreen & Viral/Trend) ready for instant 1-click radar evaluation.
"""

from typing import List, Dict, Any, Optional


CURATED_PRODUCTS: List[Dict[str, Any]] = [
    {
        "id": "prod_lumbar_01",
        "name": "Corrector Lumbar Ergonómico Pro",
        "category": "Salud & Ergonomía (Evergreen)",
        "product_type": "Evergreen",
        "cost_unit": 8.50,
        "target_price": 39.99,
        "wow_factor": 8,
        "pain_passion": 9,
        "offline_scarcity": 8,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Trabajadores remotos, personas con dolor de espalda y choferes",
        "core_pain": "dolor lumbar crónico y mala postura al estar sentado más de 6 horas al día",
        "main_benefit": "aliviar la tensión en la columna y corregir la postura en 15 minutos diarios",
        "dropship_platform": "CJ Dropshipping / Zendrop (Envío Express 7-10 días a US/Europa)",
        "china_keywords": "Lumbar support back traction massager decompression belt",
        "description": "Dispositivo ergonómico de descompresión lumbar con puntos de acupresión ajustables.",
    },
    {
        "id": "prod_sleep_02",
        "name": "Almohada Cervical Ortopédica DeepSleep",
        "category": "Salud & Ergonomía (Evergreen)",
        "product_type": "Evergreen",
        "cost_unit": 9.80,
        "target_price": 44.99,
        "wow_factor": 7,
        "pain_passion": 9,
        "offline_scarcity": 7,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Personas con insomnio, dolor cervical y contracturas matutinas",
        "core_pain": "despertar con rigidez en el cuello, migrañas y dolor cervical constante",
        "main_benefit": "alinear la columna cervical y disfrutar de un descanso profundo sin dolores",
        "dropship_platform": "CJ Dropshipping / Wiio (Packaging al vacío para reducir volumen)",
        "china_keywords": "Memory foam contour cervical orthopedic pillow",
        "description": "Espuma con memoria viscoelástica contorneada de rebote lento con funda transpirable.",
    },
    {
        "id": "prod_vacuum_03",
        "name": "Sellador al Vacío Portátil USB + Bolsas Reutilizables",
        "category": "Gadgets de Cocina / Hogar (Evergreen)",
        "product_type": "Evergreen",
        "cost_unit": 6.20,
        "target_price": 34.99,
        "wow_factor": 8,
        "pain_passion": 8,
        "offline_scarcity": 8,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Familias, amantes del orden en cocina y meal-preppers",
        "core_pain": "comida que se echa a perder rápido y espacio saturado en la nevera",
        "main_benefit": "mantener los alimentos frescos 5 veces más tiempo y ahorrar cientos de dólares",
        "dropship_platform": "CJ Dropshipping / DSers AliExpress",
        "china_keywords": "Mini handheld electric vacuum sealer USB rechargeable with bags",
        "description": "Sellador compacto inalámbrico para conservar carnes, vegetales y snacks frescos.",
    },
    {
        "id": "prod_cutter_04",
        "name": "Procesador & Cortador Eléctrico 4-en-1 Multifunción",
        "category": "Gadgets de Cocina / Hogar (Evergreen)",
        "product_type": "Evergreen",
        "cost_unit": 5.50,
        "target_price": 29.99,
        "wow_factor": 9,
        "pain_passion": 8,
        "offline_scarcity": 8,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Cocineros caseros y personas con poco tiempo para picar alimentos",
        "core_pain": "perder 30 minutos picando cebollas con olor y ensuciando múltiples cuchillos",
        "main_benefit": "picar, triturar y pelar cualquier alimento en 3 segundos con 1 solo botón",
        "dropship_platform": "DSers AliExpress / CJ Dropshipping",
        "china_keywords": "Handheld electric vegetable cutter 4 in 1 wireless garlic mud masher",
        "description": "Picador inalámbrico con orificio abierto de carga continua y cepillo de limpieza.",
    },
    {
        "id": "prod_crystal_05",
        "name": "Depiladora de Cristal Nano Indolora Reutilizable",
        "category": "Belleza & Cuidado Personal",
        "product_type": "Viral/Trend",
        "cost_unit": 2.20,
        "target_price": 24.99,
        "wow_factor": 9,
        "pain_passion": 8,
        "offline_scarcity": 9,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Mujeres y jóvenes que buscan depilación sin irritación ni químicos",
        "core_pain": "irritaciones por afeitadoras convencionales y tratamientos de cera dolorosos",
        "main_benefit": "eliminar el vello corporal al instante y exfoliar la piel sin dolor ni cortes",
        "dropship_platform": "CJ Dropshipping / Dropi (Ideal para contraentrega COD)",
        "china_keywords": "Nano crystal physical hair eraser painless hair remover",
        "description": "Herramienta de depilación física por micro-fricción que exfolia y retira vello.",
    },
    {
        "id": "prod_facial_06",
        "name": "Dispositivo de Microcorriente Facial & Terapia LED",
        "category": "Belleza & Cuidado Personal",
        "product_type": "Evergreen",
        "cost_unit": 7.50,
        "target_price": 49.99,
        "wow_factor": 8,
        "pain_passion": 9,
        "offline_scarcity": 8,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Mujeres y hombres interesados en skincare, anti-edad y lifting facial",
        "core_pain": "aparición de arrugas, líneas de expresión y flacidez en el cuello/rostro",
        "main_benefit": "reafirmar la piel y reducir líneas de expresión con sesiones de 5 minutos en casa",
        "dropship_platform": "Zendrop / CJ Dropshipping",
        "china_keywords": "Facial neck lifting EMS microcurrent LED photon therapy massager",
        "description": "Masajeador facial ergonómico con calor térmico, microcorriente EMS y 3 modos de luz LED.",
    },
    {
        "id": "prod_carvac_07",
        "name": "Mini Aspiradora Inalámbrica 2-en-1 de Alta Succión",
        "category": "Organización & Limpieza",
        "product_type": "Evergreen",
        "cost_unit": 7.80,
        "target_price": 39.99,
        "wow_factor": 9,
        "pain_passion": 8,
        "offline_scarcity": 7,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Dueños de vehículos, amantes de la limpieza y trabajadores de oficina",
        "core_pain": "migajas y polvo acumulado en ranuras difíciles del auto y teclado",
        "main_benefit": "limpiar a fondo rincones imposibles en segundos con potencia ciclónica sin cables",
        "dropship_platform": "CJ Dropshipping / AutoDS",
        "china_keywords": "Wireless portable handheld vacuum cleaner high suction blower 2 in 1",
        "description": "Aspirador soplador recargable USB tipo C con boquillas intercambiables.",
    },
    {
        "id": "prod_tripod_08",
        "name": "Trípode Inteligente con Seguimiento Facial IA 360°",
        "category": "Viral TikTok / Gadgets Wow",
        "product_type": "Viral/Trend",
        "cost_unit": 8.90,
        "target_price": 49.99,
        "wow_factor": 10,
        "pain_passion": 8,
        "offline_scarcity": 9,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Creadores de contenido, streamers, profesores online y TikTokers",
        "core_pain": "depender de otra persona para grabar o tener que acomodar la cámara continuamente",
        "main_benefit": "grabar videos profesionales con la cámara siguiéndote en 360° sin necesidad de app",
        "dropship_platform": "CJ Dropshipping / Zendrop",
        "china_keywords": "Auto face tracking gimbal 360 rotation smart shooting phone holder",
        "description": "Gimbal de seguimiento automático con cámara integrada por reconocimiento gestual.",
    },
    {
        "id": "prod_lamp_09",
        "name": "Lámpara de Levitación Magnética con Carga Inalámbrica",
        "category": "Viral TikTok / Gadgets Wow",
        "product_type": "Viral/Trend",
        "cost_unit": 13.50,
        "target_price": 69.99,
        "wow_factor": 10,
        "pain_passion": 6,
        "offline_scarcity": 10,
        "has_size_variants": False,
        "is_fragile": True,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Entusiastas del diseño de interiores, setup de escritorio y regalos premium",
        "core_pain": "decoración aburrida y escritorios llenos de cables desordenados",
        "main_benefit": "transformar cualquier espacio con un foco flotante hipnótico y carga rápida para celular",
        "dropship_platform": "CJ Dropshipping / Agente Privado (Requiere empaque protector reforzado)",
        "china_keywords": "Magnetic levitation light bulb wireless charging floating desk lamp",
        "description": "Foco LED flotante por suspensión magnética con base de madera y cargador Qi inalámbrico.",
    },
    {
        "id": "prod_wrist_10",
        "name": "Mousepad Ergonómico Deslizante con Soporte de Muñeca",
        "category": "Accesorios de Oficina / Trabajo",
        "product_type": "Evergreen",
        "cost_unit": 3.80,
        "target_price": 24.99,
        "wow_factor": 7,
        "pain_passion": 9,
        "offline_scarcity": 8,
        "has_size_variants": False,
        "is_fragile": False,
        "is_heavy": False,
        "is_battery": False,
        "audience": "Gamers, programadores y oficinistas con fatiga en la muñeca",
        "core_pain": "síndrome del túnel carpiano y dolor punzante en la muñeca tras largas horas de mouse",
        "main_benefit": "deslizar la mano con cero fricción y eliminar la fatiga articular por completo",
        "dropship_platform": "DSers AliExpress / CJ Dropshipping",
        "china_keywords": "Gliding wrist rest pad for mouse ergonomic palm rest",
        "description": "Reposamuñecas ergonómico móvil con patines de teflón y base acolchada viscoelástica.",
    }
]


class ProductCatalog:
    """
    Search and filtering utilities for curated and custom candidate products.
    """

    @staticmethod
    def get_all_categories() -> List[str]:
        categories = sorted(list(set(p["category"] for p in CURATED_PRODUCTS)))
        return ["Todas las Categorías"] + categories

    @staticmethod
    def search_products(
        category: str = "Todas las Categorías",
        product_type: str = "Todos",  # 'Todos', 'Evergreen', 'Viral/Trend'
        search_query: str = "",
        max_cost: Optional[float] = None,
        min_multiplier: float = 0.0,
    ) -> List[Dict[str, Any]]:
        results = []
        for p in CURATED_PRODUCTS:
            # Filter category
            if category != "Todas las Categorías" and p["category"] != category:
                continue

            # Filter type
            if product_type != "Todos" and p["product_type"] != product_type:
                continue

            # Filter max cost
            if max_cost is not None and p["cost_unit"] > max_cost:
                continue

            # Filter multiplier
            multiplier = p["target_price"] / p["cost_unit"]
            if multiplier < min_multiplier:
                continue

            # Filter search query
            if search_query:
                q = search_query.lower()
                text_corpus = f"{p['name']} {p['category']} {p['audience']} {p['core_pain']} {p['description']}".lower()
                if q not in text_corpus:
                    continue

            results.append(p)

        return results

    @staticmethod
    def get_product_by_id(product_id: str) -> Optional[Dict[str, Any]]:
        for p in CURATED_PRODUCTS:
            if p["id"] == product_id:
                return p
        return None
