# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    cr_payment_method_icon = fields.Boolean(string='Payment Icon')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cr_payment_method_icon = fields.Boolean(related='pos_config_id.cr_payment_method_icon',readonly=False)

