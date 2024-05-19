from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    il_id = fields.Many2one('hr.department', string='İl', domain=[('department_type_id.name', '=', 'İl')])
    ilce_id = fields.Many2one('hr.department', string='İlçe', domain=[('department_type_id.name', '=', 'İlçe')])
    lise_id = fields.Many2one('hr.department', string='Lise', domain=[('department_type_id.name', '=', 'Lise')])

    @api.model
    def create(self, vals):
        if 'il_id' in vals:
            vals['il_id'] = int(vals['il_id'])
        if 'ilce_id' in vals:
            vals['ilce_id'] = int(vals['ilce_id'])
        if 'lise_id' in vals:
            vals['lise_id'] = int(vals['lise_id'])
        user = super(ResUsers, self).create(vals)
        user.karma += 1  # Kullanıcıya başlangıç karma puanı ver
        return user
