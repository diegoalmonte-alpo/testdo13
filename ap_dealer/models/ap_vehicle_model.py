
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
    image = fields.Image("Logo", attachment=True,
        help="This field holds the image used as logo for the brand, limited to 1024x1024px.")
    image_medium = fields.Image("Medium-sized image", attachment=True,
        help="Medium-sized logo of the brand. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Image("Small-sized image", attachment=True,
        help="Small-sized logo of the brand. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")

#    @api.model_create_multi
#    def create(self, vals_list):
#        for vals in vals_list:
#            tools.image_resize_images(vals)
#        return super(FleetVehicleModelBrand, self).create(vals_list)

#    def write(self, vals):
#        tools.image_resize_images(vals)
#        return super(FleetVehicleModelBrand, self).write(vals)
