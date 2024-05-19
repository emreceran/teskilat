from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from werkzeug.utils import redirect as werkzeug_redirect
import logging

_logger = logging.getLogger(__name__)

class SignupController(Home):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        res = super(SignupController, self).web_auth_signup(*args, **kw)
        departments = request.env['hr.department'].search([])
        res.qcontext.update({
            'departments': departments
        })
        return res

    @http.route('/get_districts', type='json', auth='public', website=True)
    def get_districts(self, il_id):
        try:
            il_id = int(il_id)
            districts = request.env['hr.department'].search([('parent_id', '=', il_id), ('department_type', '=', 'ilce')])
            return [{'id': d.id, 'name': d.name} for d in districts]
        except Exception as e:
            _logger.error('Error in get_districts: %s', e)
            return {'error': str(e)}

    @http.route('/get_schools', type='json', auth='public', website=True)
    def get_schools(self, ilce_id):
        try:
            ilce_id = int(ilce_id)
            schools = request.env['hr.department'].search([('parent_id', '=', ilce_id), ('department_type', '=', 'lise')])
            return [{'id': s.id, 'name': s.name} for s in schools]
        except Exception as e:
            _logger.error('Error in get_schools: %s', e)
            return {'error': str(e)}

    @http.route('/web/login', type='http', auth='public', website=True)
    def web_login(self, redirect=None, **kw):
        if request.httprequest.method == 'POST':
            login = kw.get('login')
            password = kw.get('password')
            uid = request.session.authenticate(request.session.db, login, password)
            if uid:
                return werkzeug_redirect('/profile/user/%d' % uid)
        return super(SignupController, self).web_login(redirect, **kw)
