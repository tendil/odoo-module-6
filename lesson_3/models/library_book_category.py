from odoo import fields, models

class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'

    def action_show_category_books(self):
        """ Display in the pop-up window a list of
        books that belong to that category"""
        self.ensure_one()
        return {
            'name': 'Category Books',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'library.book',
            'target': 'new',
            'domain': [('category_id', '=', self.id)]
        }
