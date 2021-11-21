# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.bus.controllers.main import BusController

class BusController(BusController):
    # @http.route('/api/longpolling/send', type='json', auth='public')
    @http.route('/api/longpolling/send', type="http", methods=['POST'], auth='public', csrf=False)
    def api_send(self, channel=False, message=False, **post):
        return self.send(channel, message)

    @http.route('/api/longpolling/poll', type="http", methods=['POST'], auth='public', csrf=False)
    def api_poll(self, channels, last, options=None):
        return self.poll(channels, last, options)

    @http.route('/my_website/my_website/objects/', auth='public')
    def list(self, **kw):
        return "asfsfsdfdf"

#     @http.route('/my_website/my_website/objects/<model("my_website.my_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_website.object', {
#             'object': obj
#         })
