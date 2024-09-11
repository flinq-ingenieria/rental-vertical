# Part of rental-vertical See LICENSE file for full copyright and licensing details.

{
    "name": "Rental Contract day",
    "summary": "Extension of module rental_contract and rental_pricelist",
    "description": """
During longtime rentals, it is often required to write invoices in regular intervals.
This is possible with the contract module, which is here extended to support rental
use cases in extension to purchase and sale use cases.

If a product is rentable in days, the related rental service is automatically
considered as a contract and linked to the standard customer contract template.
If you add this daily rental service in a sale order and confirm it, a contract
is automatically created.
""",
    "usage": """
- Create a stockable product and mark it as rentable in months.
  The automatically created rental service has the flag 'Is a contract' = True.
- Create a sale order, add the rental service and confirm the order.
  A contract is automatically created.


 - rental_contract
 - rental_pricelist
    """,
    "version": "15.0.1.0.0",
    "category": "Rental",
"author": "zvERP.com, elego Software Solutions GmbH, Odoo Community Association (OCA)",
    "depends": [
        "rental_contract",
        "rental_pricelist",
        "rental_offday"
    ],
    "data": [],
    "demo": [],
    "qweb": [],
    "auto_install": False,
    "license": "AGPL-3",
}
