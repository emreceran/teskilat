from odoo import models, fields, api

class Department(models.Model):
    _inherit = 'hr.department'

    department_type = fields.Selection([
        ('il', 'İl'),
        ('ilce', 'İlçe'),
        ('lise', 'Lise')
    ], string='Department Type', required=True)

    parent_department_type = fields.Char(string='Parent Department Type', compute='_compute_parent_department_type', store=True)

    @api.depends('parent_id')
    def _compute_parent_department_type(self):
        for record in self:
            record.parent_department_type = record.parent_id.department_type if record.parent_id else ''
