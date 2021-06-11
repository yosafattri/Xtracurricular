# -*- coding: utf-8 -*-
{
    'name': "Xtracurricular",

    'summary': """
        Document extracurriculars, its sessions, and members.
    """,

    'description': """
        Tihs module can be used to assist in documenting extracurriculars, its sessions, and members.
    """,

    'author': "Group 10 Teratai Jaya",
    'website': "http://www.terataijaya.my.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/role.xml',
        # 'views/extracurricular.xml',
        'views/templates.xml',
        'views/session.xml',
        'views/member.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application' : True,
    
}