{
    'name': 'Lesson 6-3',
    'version': '17.0.1.0',
    'category': 'Extra Tools',
    'summary': """Odoo - Lesson 6-3.""",
    'license': 'OPL-1',
    'author': 'Dmitry Meita',
    'website': 'https://tjhelpers.com',
    'depends': [
        'mail',
        'lesson_4',
    ],
    'data': [
        'data/ir_cron_data.xml',
        'views/library_author_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
