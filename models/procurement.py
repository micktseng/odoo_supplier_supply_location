#-*- coding: utf-8 -*-
from odoo import models, api, _

class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    # TDE FIXME: 無法產生正確會計分路
    @api.multi
    def make_po(self):
        res = []
        for procurement in self:
            suppliers = procurement.product_id.seller_ids.filtered(
                lambda r: r.location_id == procurement.location_id)
            if suppliers:
                todo_suppliers = suppliers.copy({
                    'sequence': -9999
                })

                procurement.product_id.refresh()
                res += super(ProcurementOrder, procurement).make_po()
                todo_suppliers.unlink()
            else:
                res += super(ProcurementOrder, procurement).make_po()


        return res
