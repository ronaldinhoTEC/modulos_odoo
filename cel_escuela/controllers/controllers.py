# -*- coding: utf-8 -*-
# from odoo import http


# class CelEscuela(http.Controller):
#     @http.route('/cel_escuela/cel_escuela/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cel_escuela/cel_escuela/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cel_escuela.listing', {
#             'root': '/cel_escuela/cel_escuela',
#             'objects': http.request.env['cel_escuela.cel_escuela'].search([]),
#         })

#     @http.route('/cel_escuela/cel_escuela/objects/<model("cel_escuela.cel_escuela"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cel_escuela.object', {
#             'object': obj
#         })
