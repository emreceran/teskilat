from odoo import models, fields, api

class Department(models.Model):
    _inherit = 'hr.department'

    department_type = fields.Selection([
        ('il', 'İl'),
        ('ilce', 'İlçe'),
        ('lise', 'Lise')
    ], string='Department Type', required=True)

    il_id = fields.Many2one('hr.department', string='İl', domain=[('department_type', '=', 'il')])
    ilce_id = fields.Many2one('hr.department', string='İlçe', domain=[('department_type', '=', 'ilce')])

    @api.depends('parent_id')
    def _compute_parent_department_type(self):
        for record in self:
            record.parent_department_type = record.parent_id.department_type if record.parent_id else ''

    @api.onchange('department_type')
    def _onchange_department_type(self):
        if self.department_type == 'ilce':
            return {'domain': {'parent_id': [('department_type', '=', 'il')], 'il_id': [('department_type', '=', 'il')], 'ilce_id': []}}
        elif self.department_type == 'lise':
            return {'domain': {'parent_id': [('department_type', 'in', ['il', 'ilce'])], 'il_id': [('department_type', '=', 'il')], 'ilce_id': [('department_type', '=', 'ilce')]}}
        else:
            return {'domain': {'parent_id': [], 'il_id': [], 'ilce_id': []}}
