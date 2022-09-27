# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.library15.controllers.home import Books

class InheritedBooks(Books):

    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get("available"):
            all_books = response.qcontext["books"]
            available_books = all_books.filtered(
                "is_available"
            )
            response.qcontext["books"] = available_books
        return response
