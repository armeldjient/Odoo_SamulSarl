# -*- coding: utf-8 -*-
from odoo import fields, models

class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    payment_icon_image = fields.Image(string="Logo", max_width=128, max_height=128)