{
    'name': 'Todo App',
    'version': '1.0',
    'summary': 'Simple Todo Application',
    'description': 'A simple todo application for Odoo',
    'category': 'Productivity',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
