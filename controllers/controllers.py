# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.bus.controllers.main import BusController
from odoo.http import request
import werkzeug

from odoo.addons.link_tracker.controller.main import LinkTracker


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


class LinkTracker(LinkTracker):

    @http.route()
    def full_url_redirect(self, code, **post):
        country_code = request.session.geoip and request.session.geoip.get('country_code') or False
        sid = request.session.sid
        request.env['link.tracker.click'].sudo().add_click(
            code,
            ip=request.httprequest.remote_addr,
            country_code=country_code,
            sid=sid
        )
        redirect_url = request.env['link.tracker'].get_url_from_code(code)
        return werkzeug.utils.redirect(redirect_url or '', 301)