from odoo import http
from odoo.http import request
import base64

class ProfileController(http.Controller):

    @http.route('/profile/edit', type='http', auth="user", website=True)
    def view_user_profile_edition(self, **kwargs):
        user_id = int(kwargs.get('user_id', 0))
        departments = request.env['hr.department'].search([])

        if user_id and request.env.user.id != user_id and request.env.user._is_admin():
            user = request.env['res.users'].browse(user_id)
            values = self._prepare_user_values(searches=kwargs, user=user, is_public_user=False)
        else:
            values = self._prepare_user_values(searches=kwargs)

        values.update({
            'email_required': kwargs.get('email_required'),
            'departments': departments,
            'url_param': kwargs.get('url_param'),
        })
        return request.render("website_profile.user_profile_edit_main", values)

    def _prepare_user_values(self, searches=None, user=None, is_public_user=True):
        user = user or request.env.user
        values = {
            'user': user,
            'is_public_user': is_public_user,
        }
        return values

    @http.route('/profile/save', type='http', auth='user', website=True)
    def profile_save(self, **kwargs):
        user = request.env.user
        il_id = kwargs.get('il_id')
        ilce_id = kwargs.get('ilce_id')
        lise_id = kwargs.get('lise_id')

        values = {
            'il_id': int(il_id) if il_id else False,
            'ilce_id': int(ilce_id) if ilce_id else False,
            'lise_id': int(lise_id) if lise_id else False,
        }

        user.write(values)
        return request.redirect('/profile/user/%s' % user.id)

    def _profile_edition_preprocess_values(self, user, **kwargs):
        values = {
            'name': kwargs.get('name'),
            'website': kwargs.get('website'),
            'email': kwargs.get('email'),
            'website_description': kwargs.get('description'),
            'il_id': int(kwargs.get('il_id')) if kwargs.get('il_id') else False,
            'ilce_id': int(kwargs.get('ilce_id')) if kwargs.get('ilce_id') else False,
            'lise_id': int(kwargs.get('lise_id')) if kwargs.get('lise_id') else False,
        }

        if 'clear_image' in kwargs:
            values['image_1920'] = False
        elif kwargs.get('ufile'):
            image = kwargs.get('ufile').read()
            values['image_1920'] = base64.b64encode(image)

        if request.uid == user.id:  # the controller allows to edit only its own privacy settings; use partner management for other cases
            values['website_published'] = kwargs.get('website_published') == 'True'
        return values
