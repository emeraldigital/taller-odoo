# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    # Model's description fields
    _name = "library.book"
    _description = "Book"
    
    # Model's fields
    name = fields.Char(
        string="Title",
        required=True
    )
    active = fields.Boolean(
        string = "Is active?",
        default=True
    )
    publisher_id = fields.Many2one(
        "res.partner",
        string="Publisher"
    )
    author_ids = fields.Many2many(
        "res.partner",
        string="Authors"
    )
    isbn = fields.Char("ISBN")
    date_published = fields.Date()
    image = fields.Binary("Cover")

    # Model's methods
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
        else:
          return False

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid!" % book.isbn)
            # Odoo recommendation to RPC calls
            return True
