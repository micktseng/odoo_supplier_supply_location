from odoo import fields, models

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    location_id = fields.Many2one('stock.location', string="Customer Location", company_dependent=True,
                                  domain = [('usage','=','internal')])
