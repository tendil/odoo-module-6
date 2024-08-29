{
    'name': 'Lesson 6-2',
    'version': '17.0.1.0',
    'category': 'Extra Tools',
    'summary': """Odoo - Lesson 6-2.""",
    'license': 'OPL-1',
    'author': 'Dmitry Meita',
    'website': 'https://tjhelpers.com',
    'depends': [
        'lesson_1',
    ],
    'data': [
        'security/library_book_groups.xml',
        'security/ir.model.access.csv',
        'security/library_book_security.xml',
        'views/library_author_views.xml',
        'views/library_book_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
