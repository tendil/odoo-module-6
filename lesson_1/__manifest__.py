{
    'name': 'Lesson 6-1',
    'version': '17.0.1.0',
    'category': 'Extra Tools',
    'summary': """Odoo - Lesson 6-1.""",
    'license': 'OPL-1',
    'author': 'Dmitry Meita',
    'website': 'https://tjhelpers.com',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/library_book_menus.xml',
        'views/library_book_views.xml',
        'data/library_book_data.xml',
        'data/library_book_demo.xml',
        'data/library_book_edit_data.xml',
    ],
    'demo': [
        'data/res_partner_demo.xml',
        'data/res_partner_bank_demo.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
