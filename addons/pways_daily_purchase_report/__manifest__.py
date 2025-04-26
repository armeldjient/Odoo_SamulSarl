# -*- coding: utf-8 -*-
{
    'name': 'Periodic Purchase Report',
    'version': '16.0.0',
    'category': 'Purchase',
    'author': 'Preciseways',
    'website': "https://www.preciseways.com",
    'summary': "Day Wise Purchase Report | Purchase day wise | Purchase day book | Day Wise Report | Monthly Report | Weekly Report | Purchase Daily Report | Purchase Report | Purchase | Periodic purchase information on basic of vendors",
    'description': """Information about all purchase products vendors wise in the period of daily, weekly and monthly""",
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/daily_purchase_report_view.xml',
        'report/report.xml',
        'report/daily_purchase_report_template.xml'
    ],
    'application': True,
    'installable': True,
    'images':['static/description/banner.png'],
    'license': 'OPL-1',
}
