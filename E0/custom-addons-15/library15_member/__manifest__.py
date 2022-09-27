# -*- coding: utf-8 -*-
{
    'name': "library15_member",

    'summary': "Manage members' borrowing books.",

    'author': "Sergio Ernesto Tostado Sánchez",
    'website': "http://www.yourcompany.com",
    'category': 'Service/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'library15',
        'mail'
    ],

    # always loaded
    'data': [
        'security/inherited_res_groups.xml',
        'security/ir.model.access.csv',
        'views/inherited_library_book_views.xml',
        'views/menus.xml',
        'views/library_member_views.xml',
        'views/inherited_home_controller_template.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'license': 'AGPL-3',
    'application': False
}
