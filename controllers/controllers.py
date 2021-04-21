# -*- coding: utf-8 -*-
# from odoo import http


# class MyWebsite(http.Controller):
#     @http.route('/my_website/my_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_website/my_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_website.listing', {
#             'root': '/my_website/my_website',
#             'objects': http.request.env['my_website.my_website'].search([]),
#         })

#     @http.route('/my_website/my_website/objects/<model("my_website.my_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_website.object', {
#             'object': obj
#         })
