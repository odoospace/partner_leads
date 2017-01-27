# -*- coding: utf-8 -*-
{
    'name': "Partner Leads",

    'summary': """
        The aim is to show how many leads each partern has got.""",

    'description': """
        It allows to show lead number as smart button in the partner form.
        Extend the crm module.
    """,

    'author': "Impulzia",
    'website': "http://www.impulzia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'crm',
                'resource',   
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}