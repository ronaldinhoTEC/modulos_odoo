# -*- coding: utf-8 -*-
{
    'name': "cel_escuela",

    'summary': """
        Este modulo adjunta la informacion basica de las escuelas""",

    'description': """
        Este modulo guarda, recopila, ordena y proporciona valiosa informacion sobre los colegios
    """,

    'author': "ronaldinhoTEC",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mis modulos',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
