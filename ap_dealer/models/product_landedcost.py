from odoo import api,fields, models
from odoo import tools

class Product_landedcost(models.Model):

    _name = "product.landedcost.view"
    _auto = False
    _description = "Landed Cost de Productos"

    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Char(string='Nombre')
    picking_name = fields.Char(string='Envio')
    lc_name = fields.Char(string='Costes en Destino')
    price_unit = fields.Float('Monto', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, 'product_landedcost_view')
        self._cr.execute("""
            CREATE OR REPLACE VIEW product_landedcost_view AS (
                SELECT
                  row_number() OVER () AS id, 
                  stock_landed_cost_lines.name, 
                  stock_landed_cost_lines.price_unit, 
                  stock_picking.name picking_name,
                  stock_landed_cost.name lc_name, 
                  stock_move.product_id
                FROM 
                  stock_picking, 
                  stock_move, 
                  stock_landed_cost, 
                  stock_landed_cost_stock_picking_rel, 
                  stock_landed_cost_lines
                WHERE 
                  stock_picking.id = stock_move.picking_id AND
                  stock_landed_cost_stock_picking_rel.stock_picking_id = stock_picking.id AND
                  stock_landed_cost_stock_picking_rel.stock_landed_cost_id = stock_landed_cost.id AND
                  stock_landed_cost_lines.cost_id = stock_landed_cost.id AND stock_landed_cost.state = 'done'
            )""")