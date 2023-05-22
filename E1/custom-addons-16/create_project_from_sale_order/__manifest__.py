# -*- coding: utf-8 -*-
{
    'name': "create_project_from_sale_order",

    'summary': "Create a project for a confirmed sale.",

    'description': """
        CREATE PROJECT FROM SALE ORDER
        create_project_from_sale_order

        Create a project automatically for confirmed sales.
    """,

    'author': "Sergio Ernesto Tostado Sánchez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'project',
        'mail'
    ],

    # always loaded
    'data': [
        # 'views/inherited_project_project_views.xml',
        # 'views/inherited_sale_order_views.xml'
    ],
    'application': False,
    'license': 'LGPL-3'
}