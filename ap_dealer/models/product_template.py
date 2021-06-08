
from odoo import models, fields, api, _

class Product(models.Model):
    _inherit = 'product.template'

    def get_cotizaciones(self):
        count = self.env['sale.order.line'].search_count([('product_id', '=', self.id)])
        self.cotizacion_count = count

    ap_vehiculo_ok = fields.Boolean(string="Es un Vehículo", default=False)
    ap_placa = fields.Char(string='Placa', help='Placa del Vehiculo')
    ap_chasis = fields.Char(string='Chasis', help='Número Chasis del Vehiculo')
    ap_ano = fields.Char(string='Año', help='Año del Vehiculo')

    ap_condicion = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado')
    ], 'Condicion', help='Condición del Vehículo')

    ap_fuel_type = fields.Selection([
        ('gasoline', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('glp', 'GLP'),
        ('ng', 'Gas Natural'),
        ('electric', 'Electrico'),
        ('hybrid', 'Hybrid')
    ], 'Tipo de Combustible', help='Combustible utilizado por el Vehículo')

    ap_tipo_vehiculo = fields.Selection([
        ('sedan', 'Sedán'),
        ('compacto', 'Compacto'),
        ('jeepeta', 'Jeepeta'),
        ('camioneta', 'Camioneta'),
        ('coupe', 'Coupé/Sport'),
        ('barcos', 'Barcos'),
        ('camion', 'Camión'),
        ('autobus', 'Autobus'),
        ('pesado', 'Pesado/Maquinaria'),
        ('motores', 'Motores')
    ], 'Tipo de Vehículo ', help='Tipo o Clasificación de Vehículo')

    ap_traccion = fields.Selection([
        ('delantera', 'Delantera'),
        ('trasera', 'Trasera'),
        ('2wd', '2WD'),
        ('4wd', '4WD'),
        ('4wdft', '4WD Full Time'),
        ('awd', 'AWD')
    ], 'Tipo de Tracción ', help='Tipo de Tracción del Vehículo')

    ap_color = fields.Char('Color Exterior',help='Color Exterior')
    ap_color_interior = fields.Char('Color Interior', help='Color Interior')
    ap_motor = fields.Char('Motor', help='Color Interior')
    ap_fecha_registro = fields.Date('Fecha de Registro', required=False,default=fields.Date.today, help='Fecha de Ingreso del Vehículo')
    ap_seats = fields.Integer('Asientos', help='Cantidad de Asientos')
    ap_horsepower = fields.Integer('Caballos', help='Caballos de Potencia')
    ap_cilindros = fields.Integer('Cilindros', help='Cilindros')
    ap_capacidad_carga = fields.Integer('Capacidad de Carga', help='Capacidad de Carga en Lb')
    ap_doors = fields.Integer('Puertas', help='Cantidad de Puertas', default=4)
    ap_odometer = fields.Float(string='Ultimo Odometro', help='Medida del Odómetro del Vehiculo')
    ap_odometer_unit = fields.Selection([
        ('kilometros', 'Kilometros'),
        ('millas', 'Millas')
    ], 'Unidad Odometro', default='kilometros', help='Unidad del odómetro ')
    ap_transmission = fields.Selection([
        ('manual', 'Manual'),
        ('automatic', 'Automatica'),
        ('sincronizada', 'Sincronizada'),
        ('semiautomatica', 'Semiautomatica')
    ], 'Transmisión', help='Tipo de Transmision del vehiculo')

    model_id = fields.Many2one('ap.vehicle.model', 'Modelo', track_visibility="onchange", help='Modelo del Vehiculo')
    brand_id = fields.Many2one('ap.vehicle.model.brand', 'Marca', related="model_id.brand_id", store=True, readonly=False, help='Marca del Vehiculo')

    ap_tercerafila = fields.Boolean(string="Tercera Fila Asientos", default=False)
    ap_baulelectrico = fields.Boolean(string="Baul Eléctricoo", default=False)
    ap_asientospiel = fields.Boolean(string="Asientos en Piel", default=False)
    ap_sunroof = fields.Boolean(string="Sunroof", default=False)
    ap_techopanoramico = fields.Boolean(string="Techo Panorámico", default=False)
    ap_llaveinteligente = fields.Boolean(string="Llave Inteligente/Encendido", default=False)
    ap_radioamfm = fields.Boolean(string="Radio AM/FM", default=False)
    ap_radiomultimedia = fields.Boolean(string="Radio Multimedia", default=False)
    ap_halogenos = fields.Boolean(string="Faros Halogenos/Xenon", default=False)
    ap_navegacion = fields.Boolean(string="Sistema Navegación", default=False)
    ap_camarareversa = fields.Boolean(string="Cámara Reversa", default=False)
    ap_alarma = fields.Boolean(string="Alarma", default=False)
    ap_bolsachofer = fields.Boolean(string="Bolsa de Aire Chofer", default=False)
    ap_bolsapasajero = fields.Boolean(string="Bolsa de Aire Pasajero", default=False)
    ap_bolsatrasera = fields.Boolean(string="Bolsa de Aire Trasera", default=False)
    ap_abs = fields.Boolean(string="Frenos ABS", default=False)
    ap_seguroselectricos = fields.Boolean(string="Seguros Eléctricos", default=False)
    ap_aire = fields.Boolean(string="Aire Acondicionado", default=False)
    ap_calefaccion = fields.Boolean(string="Calefacción", default=False)
    ap_bluetooth = fields.Boolean(string="Bluetooth", default=False)
    ap_cdplayer = fields.Boolean(string="CD Player", default=False)
    ap_guiahidraulico = fields.Boolean(string="Guía Hidraulico", default=False)
    ap_guiamulti = fields.Boolean(string="Guía Multifuncional", default=False)
    ap_retrovisores = fields.Boolean(string="Retrovisores Eléctricos", default=False)
    ap_sonidopro = fields.Boolean(string="Sonido Profesional", default=False)
    ap_vidrioselec = fields.Boolean(string="Vídrios Eléctricos", default=False)
    ap_arosalum = fields.Boolean(string="Aros de Aluminio", default=False)

    ap_aire_digital = fields.Boolean(string="Aire Acondicionado Digital", default=False)
    ap_aire_doble = fields.Boolean(string="Aire Acondicionado Doble", default=False)
    ap_android_auto = fields.Boolean(string="Android Auto", default=False)
    ap_apple_carplay = fields.Boolean(string="Apple CarPlay", default=False)
    ap_asientos_deportivos = fields.Boolean(string="Asientos Deportivos", default=False)
    ap_asientos_electricos = fields.Boolean(string="Asientos Eléctricos", default=False)
    ap_asientospana = fields.Boolean(string="Asientos en Pana", default=False)
    ap_asientostela = fields.Boolean(string="Asientos en Tela", default=False)
    ap_asientosvinyl = fields.Boolean(string="Asientos en Vinyl", default=False)
    ap_cdbox = fields.Boolean(string="CD Box", default=False)
    ap_cortinaselectricas = fields.Boolean(string="Cortinas Eléctricas Traseras", default=False)
    ap_cruisecontrol = fields.Boolean(string="Cruise Control", default=False)
    ap_tractioncontrol = fields.Boolean(string="Traction Control", default=False)
    ap_dvd = fields.Boolean(string="DVD", default=False)
    ap_guiasemihidraulico = fields.Boolean(string="Guía Semi-Hidraulico", default=False)
    ap_limpiavidriotrasero = fields.Boolean(string="Limpia Vidrio Trasero", default=False)
    ap_nevera = fields.Boolean(string="Nevera", default=False)
    ap_pinturafabrica = fields.Boolean(string="Pintura de Fábrica", default=False)
    ap_puertaelectrica = fields.Boolean(string="Puerta Eléctrica", default=False)
    ap_vidriosmanual = fields.Boolean(string="Vídrios Manuales", default=False)
    ap_arosfabrica = fields.Boolean(string="Aros de Fábrica", default=False)
    ap_aroshierro = fields.Boolean(string="Aros de Hierro", default=False)
    ap_arosmagnesio = fields.Boolean(string="Aros de Magnesio", default=False)
    ap_cabinasimple = fields.Boolean(string="Cabina Simple", default=False)
    ap_cabinadoble = fields.Boolean(string="Cabina Doble", default=False)
    ap_cabinacuarta = fields.Boolean(string="Cabina y Cuarta", default=False)
    ap_cabinamedia = fields.Boolean(string="Cabina y Media", default=False)
    ap_camacerrada = fields.Boolean(string="Cama Cerrada", default=False)
    ap_camacorta = fields.Boolean(string="Cama Corta", default=False)
    ap_camalarga = fields.Boolean(string="Cama Larga", default=False)
    ap_gancho = fields.Boolean(string="Gancho Remolque", default=False)
    ap_intercooler = fields.Boolean(string="Intercooler", default=False)
    ap_lucesdiurno = fields.Boolean(string="Luces Encendido Diurno", default=False)
    ap_transmisiondeportiva = fields.Boolean(string="Transmision Deportiva", default=False)
    ap_turbo = fields.Boolean(string="Turbo", default=False)
    ap_turbodiesel = fields.Boolean(string="Turbo Diesel", default=False)
    ap_frenoshidraulicos = fields.Boolean(string="Frenos Hidráulicos", default=False)
    ap_multilock = fields.Boolean(string="Mul-t-lock", default=False)
    ap_sensoresparqueo = fields.Boolean(string="Sensores de Parqueo", default=False)
    ap_radiosatelital = fields.Boolean(string="Radio Satelital", default=False)
    ap_tirepressure = fields.Boolean(string="Monitor de Presión Neumáticos", default=False)

    cotizacion_count = fields.Integer(compute='get_cotizaciones', string='Cotizaciones')

    def action_view_cotizacion(self):
        action = self.env.ref('ap_dealer.report_all_channels_cot_action').read()[0]
        action['domain'] = [('product_tmpl_id', 'in', self.ids)]
        action['context'] = {
            'search_default_last_year': 1,
            'pivot_measures': ['product_qty'],
            'search_default_team_id': 1
        }
        return action
