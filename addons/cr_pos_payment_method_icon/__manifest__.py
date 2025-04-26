# -*- coding: utf-8 -*-
# Email: sales@creyox.com
{
    "name": "POS Payment Method Icon || POS Payment Icon || POS Payment method image || Show Payment icon on screen",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Point of Sale",
    "summary": "This apps helps you to show payment payment icon on pos screen",
    "description": """This apps helps you to show payment payment icon on pos Screen""",
    "license": "LGPL-3",
    "version": "16.0.1",
    "depends": ["point_of_sale"],
    "application": True,
   'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'cr_pos_payment_method_icon/static/src/js/**/*',
            'cr_pos_payment_method_icon/static/src/xml/**/*',
        ],
    },
    "auto_install": False,
    "installable": True,
    "images": ["static/description/banner.png", ],
    "price": 0,
    "currency": "EUR"
}
