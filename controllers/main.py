from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home
from odoo.http import request


class AuthSignupHome(Home):

    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        if request.httprequest.method == 'POST':
            il_id = kw.get('il_id')
            ilce_id = kw.get('ilce_id')
            lise_id = kw.get('lise_id')
            if il_id:
                kw['il_id'] = int(il_id)
            if ilce_id:
                kw['ilce_id'] = int(ilce_id)
            if lise_id:
                kw['lise_id'] = int(lise_id)

        response = super(AuthSignupHome, self).web_auth_signup(*args, **kw)

        ils = request.env['hr.department'].sudo().search([('department_type', '=', 'il')])
        ilces = request.env['hr.department'].sudo().search([('department_type', '=', 'ilce')])
        lises = request.env['hr.department'].sudo().search([('department_type', '=', 'lise')])

        response.qcontext.update({
            'ils': ils,
            'ilces': ilces,
            'lises': lises
        })

        return response
