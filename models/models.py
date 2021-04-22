# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crmlead(models.Model):
    _inherit = "crm.lead"
    lead_type = fields.Char("Lead Type")