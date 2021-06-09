# -*- coding: utf-8 -*-
from odoo import http

# class Xtracurricular(http.Controller):
#     @http.route('/xtracurricular/xtracurricular/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xtracurricular/xtracurricular/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xtracurricular.listing', {
#             'root': '/xtracurricular/xtracurricular',
#             'objects': http.request.env['xtracurricular.xtracurricular'].search([]),
#         })

#     @http.route('/xtracurricular/xtracurricular/objects/<model("xtracurricular.xtracurricular"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xtracurricular.object', {
#             'object': obj
#         })