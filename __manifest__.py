{
    'name': 'Teşkilat',
    'version': '1.0',
    'depends': ['base', 'hr', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/teskilat_views.xml',
        'views/department_views.xml',
        'views/signup_form.xml',
        'views/signup_templates.xml',
        'views/edit_profile_view.xml',
        'views/profile_edit_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'teskilat/static/src/js/signup.js',
        ],
    },
     'auto_install': False,
    'installable': True,
    'application': True,
}
