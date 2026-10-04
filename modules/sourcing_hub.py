"""
Sourcing Hub & Sourcing Economics Module
Compares Dropshipping vs DDP Bulk Import economics (300 to 1,000 units) and generates professional English RFQs for Alibaba/1688 suppliers.
"""

from typing import Dict, Any, List


class SourcingHub:
    """
    Handles transition economics from dropshipping validation to private label bulk import.
    """

    @staticmethod
    def calculate_margin_jump(
        sale_price: float,
        dropship_cogs_shipping: float,
        factory_fob_unit: float,
        ddp_shipping_unit: float,
        packaging_branding_unit: float = 0.80,
        local_3pl_pick_pack: float = 3.50,
        payment_gateway_pct: float = 3.5,
        target_cpa: float = 15.00,
        units_batch: int = 500,
    ) -> Dict[str, Any]:
        """
        Calculates unit economics and net margin expansion comparing Dropshipping vs DDP Bulk Import.
        """
        gateway_fee = round(sale_price * (payment_gateway_pct / 100.0), 2)

        # 1. Dropshipping Economics (Unitary)
        dropship_total_cost = round(dropship_cogs_shipping + gateway_fee + target_cpa, 2)
        dropship_net_profit = round(sale_price - dropship_total_cost, 2)
        dropship_net_margin_pct = round((dropship_net_profit / sale_price) * 100.0, 1) if sale_price > 0 else 0.0

        # 2. Bulk DDP Import Economics (Unitary)
        bulk_landed_cogs = round(factory_fob_unit + ddp_shipping_unit + packaging_branding_unit, 2)
        bulk_total_cost = round(bulk_landed_cogs + local_3pl_pick_pack + gateway_fee + target_cpa, 2)
        bulk_net_profit = round(sale_price - bulk_total_cost, 2)
        bulk_net_margin_pct = round((bulk_net_profit / sale_price) * 100.0, 1) if sale_price > 0 else 0.0

        # Batch Totals (e.g. 300, 500, 1000 units)
        units = int(units_batch)
        dropship_batch_profit = round(dropship_net_profit * units, 2)
        bulk_batch_profit = round(bulk_net_profit * units, 2)
        extra_profit_batch = round(bulk_batch_profit - dropship_batch_profit, 2)
        profit_increase_pct = round(((bulk_net_profit - dropship_net_profit) / max(0.01, dropship_net_profit)) * 100.0, 1) if dropship_net_profit > 0 else 999.0

        # Capital Required for Bulk Batch
        capital_inventory_required = round(bulk_landed_cogs * units, 2)
        roi_inventory_pct = round((bulk_batch_profit / capital_inventory_required) * 100.0, 1) if capital_inventory_required > 0 else 0.0

        return {
            "sale_price": sale_price,
            "target_cpa": target_cpa,
            "gateway_fee": gateway_fee,
            "dropship": {
                "unit_cogs_shipping": dropship_cogs_shipping,
                "total_unit_cost": dropship_total_cost,
                "net_profit_unit": dropship_net_profit,
                "net_margin_pct": dropship_net_margin_pct,
                "batch_profit": dropship_batch_profit,
            },
            "bulk_ddp": {
                "fob_unit": factory_fob_unit,
                "ddp_freight_unit": ddp_shipping_unit,
                "branding_unit": packaging_branding_unit,
                "landed_cogs": bulk_landed_cogs,
                "local_3pl": local_3pl_pick_pack,
                "total_unit_cost": bulk_total_cost,
                "net_profit_unit": bulk_net_profit,
                "net_margin_pct": bulk_net_margin_pct,
                "batch_profit": bulk_batch_profit,
                "capital_required": capital_inventory_required,
                "roi_inventory_pct": roi_inventory_pct,
            },
            "comparison": {
                "units_batch": units,
                "extra_profit_unit": round(bulk_net_profit - dropship_net_profit, 2),
                "extra_profit_batch": extra_profit_batch,
                "profit_increase_pct": profit_increase_pct,
            },
        }

    @staticmethod
    def generate_rfq_message(
        company_name: str,
        contact_name: str,
        product_name: str,
        target_destination_country: str = "United States (3PL Warehouse)",
        custom_logo: bool = True,
        custom_box: bool = True,
        barcode_labeling: bool = True,
    ) -> str:
        """
        Generates an authoritative, professional English RFQ (Request For Quotation) for Alibaba/1688 manufacturers.
        """
        rfq_text = f"""Dear Sales Team / Factory Manager,

My name is {contact_name}, Purchasing Director at {company_name}. 

We are expanding our DTC e-commerce catalog in the {target_destination_country} market and are currently sourcing qualified manufacturing partners for our upcoming private label production run of: **{product_name}**.

We would appreciate your prompt quotation based on the following specifications and tiered volumes:

### 1. Tiered Pricing Request (FOB & EXW):
Please provide unit pricing based on order volume:
- **Sample Order:** 1-2 units (air express via DHL/FedEx to evaluate build quality & finish)
- **Tier 1 (Initial Test Batch):** 300 units
- **Tier 2 (Scale Batch):** 500 units
- **Tier 3 (Full Production):** 1,000 units
- **Tier 4 (Annual Volume):** 3,000+ units

### 2. Customization & Private Label Requirements:
- **Custom Logo:** {"Yes, laser engraved or silk-screen printed on product." if custom_logo else "Standard product without logo."}
- **Custom Packaging:** {"Yes, customized matte cardboard box with full-color 4C printing and custom foam insert." if custom_box else "Standard manufacturer packaging."}
- **Barcodes & Inserts:** {"Apply UPC/EAN barcode stickers on each box + include a custom 300gsm thank-you/instruction card." if barcode_labeling else "Standard."}

### 3. Shipping & Incoterms (DDP Quote):
Please provide estimated DDP (Delivered Duty Paid - air freight and sea freight) shipping rates and transit times to our fulfillment warehouse in: **{target_destination_country}**.

### 4. Production & Quality Standards:
- What is your standard production lead time for 500 - 1,000 units?
- What are the dimensions (cm) and gross weight (kg) per master carton, and units per carton?
- Do you accept third-party pre-shipment inspections (AQL 2.5 standard) and Alibaba Trade Assurance payment terms?

Please reply with your product catalog (PDF/Excel) and your best FOB & DDP quote at your earliest convenience.

Best regards,

**{contact_name}**
Purchasing & Supply Chain Operations | {company_name}
Email / WhatsApp / WeChat Available Upon Request
"""
        return rfq_text.strip()
