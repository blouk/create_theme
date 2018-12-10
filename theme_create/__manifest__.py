# -*- coding: utf-8 -*-
{
    'name':  'Create a theme',
    'category': 'Theme/Creative',
    'summary': 'Create a theme',
    'version': '0.1',
    'description': """
Description.
    """,
    'depends': ['website_sale'],

    'data': [
        # assets views
        'views/assets.xml',
        'views/layout/product_menu.xml',
        'views/layout/product_detail.xml',
    ],

    'installable': True,
    'application': True,
}
