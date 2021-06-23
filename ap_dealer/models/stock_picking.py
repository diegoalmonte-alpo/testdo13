from odoo import models, fields, api, _

class Stock(models.Model):
    _inherit = 'stock.picking'

    ap_chasis = fields.Char(string='Chasis', help='Chasis del Vehiculo')

    @api.depends('name', 'ap_chasis')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.ap_chasis:
                name = record.name + ' - ' + record.ap_chasis
            res.append((record.id, name))
        return res

