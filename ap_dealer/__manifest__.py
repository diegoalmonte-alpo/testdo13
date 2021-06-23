# -*- coding: utf-8 -*-
#################################################################################
# Author      : Alpo Multimedia Services. (<https://alpo.com.do/>)
# Copyright(c): 2021-Present Alpo Multimedia Services, SRL.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
#################################################################################
{
  "name"                 :  "Dealer de Vehículos",
  "summary"              :  "Añade a Odoo las varialbes necesarias para registrar informacion diversa de vehiculos",
  "category"             :  "Website",
  "version"              :  "1.0",
  "sequence"             :  1,
  "author"               :  "Alpo Multimedia Services",
  "license"              :  "Other proprietary",
  "website"              :  "https://alpo.com.do",
  "description"          :  """Añade al Producto campos para identificar productos como Vehículo 
Marca
Modelo
Placa
Chasis""",
  "depends"              :  ['product','stock'],
  "data"                 :  [ 'security/ir.model.access.csv',
                              'views/product_template.xml',
                              'views/ap_vehicle_model.xml',
                              'views/stock_picking.xml',
                              'models/report_all_channels_cot_views.xml',
                              'data/fleet_cars_data.xml',],
  "images"               :  ['static/description/Banner.jpg'],
  "application"          :  True,
  "installable"          :  True,
}