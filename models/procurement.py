from openerp.osv import fields, osv
from openerp.tools.translate import _

class procurement(osv.osv):
    _inherit = 'procurement.order'

    def _get_product_supplier(self, cr, uid, procurement, context=None):

        ''' returns the main supplier of the procurement's product given as argument'''
        supplierinfo = self.pool['product.supplierinfo']

        company_supplier = supplierinfo.search(cr, uid,
            [('product_tmpl_id', '=', procurement.product_id.product_tmpl_id.id), ('location_id', '=', procurement.location_id.id), ('company_id', '=', procurement.company_id.id)], limit=1, context=context)

        

        if company_supplier:
            return supplierinfo.browse(cr, uid, company_supplier[0], context=context).name

        company_supplier = supplierinfo.search(cr, uid,
            [('product_tmpl_id', '=', procurement.product_id.product_tmpl_id.id), ('company_id', '=', procurement.company_id.id)], limit=1, context=context)

        if company_supplier:
            return supplierinfo.browse(cr, uid, company_supplier[0], context=context).name

        return procurement.product_id.seller_id
