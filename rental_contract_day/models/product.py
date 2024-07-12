# Part of rental-vertical See LICENSE file for full copyright and licensing details.

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def write(self, vals):
        template = self.env.ref("rental_contract.rental_contract_template")
        res = super(ProductProduct, self).write(vals)
        for p in self:
            if vals.get("rental_of_day", False):
                if p.product_rental_day_id:
                    p.product_rental_day_id.is_contract = True
                    p.product_rental_day_id.property_contract_template_id = (template.id)
                    #TODO algún tipo de selector
                    p.product_rental_day_id.recurring_rule_type = "monthlylastday"
        return res
