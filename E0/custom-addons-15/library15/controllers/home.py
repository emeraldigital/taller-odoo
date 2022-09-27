# -*- coding: utf-8 -*-

from odoo import http

class Books(http.Controller):

    @http.route("/library/books")
    def list(self, **kwargs):
        library_book_obj = http.request.env['library.book']
        books = library_book_obj.search([])
        return http.request.render(
            "library15.book_list_template",
            {"books": books}
        )
