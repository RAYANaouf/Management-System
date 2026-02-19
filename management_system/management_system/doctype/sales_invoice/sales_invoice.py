import frappe
from frappe.model.document import Document

class SalesInvoice(Document):

    @frappe.whitelist()
    def get_items_prices(self, items, price_list):
        """
        items: list of item codes
        price_list: price list name
        """

        prices = {}

        for item_code in items:
            price = frappe.db.get_value(
                "Item Price",
                {
                    "item_code": item_code,
                    "price_list": price_list
                },
                "rate"
            )

            prices[item_code] = price or 0

        return prices
