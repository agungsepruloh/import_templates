from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Sales Orders'),
            'template': 'import_sale_template/static/xls/sale_order_template.xlsx'
        }]
