from odoo.tests.common import TransactionCase

class TestLibraryBook(TransactionCase):

    # Settting up data for test cases
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        # Test users
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)

        # Demo data
        self.Book = self.env["library.book"]
        self.book1 = self.Book.create({
            "name": "Lord of the Flies",
            "isbn": "0-571-05686-5"
        })
    

    # Test Cases
    def test_check_isbn_legacy(self):
        """ Test 1. Check valid ISBN. """
        self.assertTrue(
            self.book1._check_isbn
        )
