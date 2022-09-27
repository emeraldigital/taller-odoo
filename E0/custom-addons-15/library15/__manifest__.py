# -*- coding: utf-8 -*-
{
    'name': "Library Management 15",
    'summary': "Manage library catalog & book lending.",
    'description': """
        Library Management 15
        =====================

        *For Odoo v15*
        --------------

        - Library catalog *management*.
        - Book *lending*.

    """,
    'author': "Sergio Ernesto Tostado Sánchez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/library_book_views.xml',
        'views/menus.xml',
        'views/home_controller_template.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/library_book.xml',
    ],

    'license': "AGPL-3",
    'application': True
}
