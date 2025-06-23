#  -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2019-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################
{
  "name"                 :  "POS Product Price Limits",
  "summary"              :  """POS Product Price Limits facilitates the Odoo admin to
                              define the maximum and minimum for a product individually. Moreover, you can restrict the POS user to enter only an amount from a defined minimum and maximum price.It also shows warning messages for different scenarios of Odoo backend and Odoo POS.POS Min and Max Price|POS Min Product Price|POS Max Product Price|POS Min Price|Max product price|Max Price Product|Min Product Price|minimum & maximum product price|POS Product Price Limits|pos  product price limit""",
  "category"             :  "Point of Sale",
  "version"              :  "1.0.0",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/odoo-pos-product-price-limits.html",
  "description"          :  """ """,
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=pos_product_price_limit&custom_url=/pos/auto",
  "depends"              :  ['point_of_sale'],
  "data"                 :  [
                              'views/pos_config.xml',
                              'views/product.xml',
                            ],
  "assets"               :  {
                              'point_of_sale.assets': [
                                "/pos_product_price_limit/static/src/js/screens.js",
                                "/pos_product_price_limit/static/src/js/popup.js",
                                "/pos_product_price_limit/static/src/css/pos.css",
                                'pos_product_price_limit/static/src/xml/pos.xml',
                              ],
                            },
  "demo"                 :  ['demo/demo.xml'],
  "images"               :  ['static/description/Banner.png'],
  "qweb"                 :  ['static/src/xml/pos.xml'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  39,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}