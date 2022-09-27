# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryMember(models.Model):
    # Model's descriptor fields
    _name = "library.member"
    _description = "Library Member"
    # NOTE: Legacy, this works fine, but the modern noration is delegate = True
    #_inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Model's fields
    card_number = fields.Char()
    partner_id = fields.Many2one(
        "res.partner",
        delegate = True,
        ondelete = "cascade",
        required = True
    )
