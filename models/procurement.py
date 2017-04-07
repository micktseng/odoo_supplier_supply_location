from odoo import models, api

class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    @api.multi
    def make_po(self):
        for procurement in self:
            suppliers = procurement.product_id.seller_ids.filtered(
                lambda x: x.location_id == procurement.location_id)

            procurement.product_id.seller_ids &= suppliers

        return super(ProcurementOrder, self).make_po()
