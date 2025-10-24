{
    'name': 'User Task Manager',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage User tasks',
    'description': 'Manage',
    'author': 'Yoel',
    'website': "https://www.site.com",
    'depends': ['base'],
    'data': [
        # Luego grupos y accesos
        'security/task_security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': False,
}