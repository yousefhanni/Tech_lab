{
    'name': 'Tech Lab',
    'version': '18.0.1.0.0',
    'summary': 'Learning and testing module for Odoo product automation',
    'description': """
Tech Lab is a learning module designed to demonstrate
basic Odoo ORM operations such as:
- Mass price updates
- Product filtering and logging
- Simple workflow state changes
- Computed stock value logic

This module is intended for educational and testing purposes.
    """,
    'author': 'JOO',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_inventory.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
