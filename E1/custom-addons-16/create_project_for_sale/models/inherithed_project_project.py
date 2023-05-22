# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    related_sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Related Sale Order"
    )