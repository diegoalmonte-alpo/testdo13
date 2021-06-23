
from odoo import api, fields, models, tools


class VehicleModel(models.Model):
    _name = 'ap.vehicle.model'
    _description = 'Modelo del Vehiculo'
    _order = 'name asc'

    name = fields.Char('Model name', required=True)
    brand_id = fields.Many2one('ap.vehicle.model.brand', 'Make', required=True, help='Make of the vehicle')
    image = fields.Binary(related='brand_id.image', string="Logo", readonly=False)
    image = fields.Image(related='brand_id.image', string="Logo", readonly=False)
    image_medium = fields.Image(related='brand_id.image_medium', string="Logo (medium)", readonly=False)
    image_small = fields.Image(related='brand_id.image_small', string="Logo (small)", readonly=False)

    @api.depends('name', 'brand_id')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.brand_id.name:
                name = record.brand_id.name + ' ' + name
            res.append((record.id, name))
        return res

    @api.onchange('brand_id')
    def _onchange_brand(self):
        if self.brand_id:
            self.image_medium = self.brand_id.image
        else:
            self.image_medium = False


class FleetVehicleModelBrand(models.Model):
    _name = 'ap.vehicle.model.brand'
    _description = 'Marca del vehiculo'
    _order = 'name asc'

    name = fields.Char('Make', required=True)
    image = fields.Image("Logo", attachment=True, max_width=1024, max_height=1024,
        help="This field holds the image used as logo for the brand, limited to 1024x1024px.")
    image_medium = fields.Image("Medium-sized image", related="image", store=True, max_width=128, max_height=128)        
    image_small = fields.Image("Small-sized image", related="image", store=True, max_width=64, max_height=64)
    
