from odoo import fields, models
from datetime import datetime, timedelta


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True, translate='True')
    last_name = fields.Char(required=True, translate='True')
    birth_date = fields.Date('Birthday')
    trainee_access = fields.Boolean(compute='_compute_trainee_access',
                                    store=True)

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)

    def _compute_trainee_access(self):
        for rec in self:
            rec.trainee_access = datetime.today() - timedelta(days=30) < rec.create_date
