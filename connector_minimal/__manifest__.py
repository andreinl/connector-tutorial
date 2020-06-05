# -*- coding: utf-8 -*-
# © 2020 Andrei Levin - Didotech srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "connector_minimal",
    'summary': """
        Minimal implementation of the connector""",

    'description': """
        Module shows Connector minimal implementation
    """,

    'author': "Didotech srl",
    'website': "http://www.didotech.com",
    'category': 'Connector',
    'version': '0.1.2.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'connector'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/connector_menu.xml',
        'views/backend_view.xml',
        'views/launcher_view.xml'
    ],

    'demo': [
        # 'demo/demo.xml',
    ],
    'external_dependencies': {
        'python': [
            'cachetools',
            'odoolib'  # pip install odoo-client-lib
        ]
    }
}
