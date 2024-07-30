# Part of rental-vertical See LICENSE file for full copyright and licensing details.
from odoo import api, models
from odoo.exceptions import UserError

import datetime
from datetime import timedelta
from dateutil.relativedelta import *

class ContractLine(models.Model):
    _inherit = "contract.line"

    def _prepare_invoice_line(self, move_form):
        def offday_calc(self, end, start):
            offday_count = 0

            for offday in self.sale_order_line_id.fixed_offday_ids:
                if start <= offday.date <= end:
                    offday_count = offday_count + 1
            for offday in self.sale_order_line_id.add_offday_ids:
                if start <= offday.date <= end:
                    offday_count = offday_count + 1
            return offday_count

        self.ensure_one()
        res = super(ContractLine, self)._prepare_invoice_line(move_form)

        start = self.next_period_date_start
        end = self.next_period_date_end

        invoice_period = (end - start)
        offday_count = offday_calc(self,end,start)
        res.update({"quantity": self.sale_order_line_id.rental_qty * (invoice_period.days + 1 - offday_count),})

        return res
