{
    'name': 'Property Management',
    'version': '15.0.1.0.0',
    'sequence': -10,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_menu_views.xml',
        'views/property_views.xml',
    ],
    'application': True,
    'installable': True
}
