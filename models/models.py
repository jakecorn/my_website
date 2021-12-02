# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crmlead(models.Model):
    _inherit = "crm.lead"
    lead_type = fields.Char("Lead Type")

class BlogPost(models.Model):
    _inherit = "blog.post"
    is_mini_guide = fields.Boolean(default=False)
    teaser = fields.Text("Teaser Description")


class LinkTrackerClick(models.Model):
    _inherit = "link.tracker.click"

    @api.model
    def add_click(self, code, **route_values):
        """ Main API to add a click on a link. """
        tracker_code = self.env['link.tracker.code'].search([('code', '=', code)])
        if not tracker_code:
            return None
        route_values['ip'] = route_values.get('sid', False)
        ip = route_values.get('ip', False)
        existing = self.search_count(['&', ('link_id', '=', tracker_code.link_id.id), ('ip', '=', ip)])
        if existing:
            return None

        route_values['link_id'] = tracker_code.link_id.id
        click_values = self._prepare_click_values_from_route(**route_values)

        return self.create(click_values)