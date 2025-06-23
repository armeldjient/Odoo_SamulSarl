# -*- coding: utf-8 -*-
#################################################################################
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#################################################################################
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    min_price = fields.Float(string="Min Price", help="Minimum Price of product.")
    enable_min_price = fields.Boolean(string="Enable Min Price", help="Enable Minimum price of product feature.",default=False)
    max_price = fields.Float(string="Max Price",help="Maximum Price of product.")
    enable_max_price = fields.Boolean(string="Enable Max Price", help="Enable Minimum price of product feature.",default=False)

    @api.constrains('enable_min_price','enable_max_price','max_price','min_price')
    def _check_max_min_price(self):
        """
            Validations for cases of min and max price of the product.
        """
        for product in self:
            if product.enable_max_price and product.max_price < product.lst_price:
                raise ValidationError('Maximum price of the product cannot be less than its sale price.')
            if (product.enable_min_price and product.min_price < 0.00) or (product.enable_max_price and product.max_price < 0.00):
                raise ValidationError('Price of the product cannot be a negative value.')
            if product.enable_min_price and product.enable_max_price and product.max_price < product.min_price:
                raise ValidationError('Max price cannot be less than min price.')
            if not product.enable_max_price and product.enable_min_price and  product.min_price > product.lst_price:
                raise ValidationError('Minimum price of the product cannot be more than its sale price.')

class PosConfig(models.Model):
    _inherit = 'pos.config'

    is_restrict_min_max_price = fields.Boolean(string="Restrict Min/Max Product Price",default=True)
   
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_is_restrict_min_max_price = fields.Boolean(related='pos_config_id.is_restrict_min_max_price',readonly=False)

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        models = super()._pos_ui_models_to_load()
        models_to_load = ["product.product"]
        for rec in models_to_load:
            if rec not in models:
                models.append(rec) 
        return models

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].extend(["min_price", "max_price","enable_min_price","enable_max_price"])
        return result  