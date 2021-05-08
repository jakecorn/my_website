# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crmlead(models.Model):
    _inherit = "crm.lead"
    lead_type = fields.Char("Lead Type")

class BlogPost(models.Model):
    _inherit = "blog.post"
    is_mini_guide = fields.Boolean(default=False)
    teaser = fields.Text("Teaser Description")