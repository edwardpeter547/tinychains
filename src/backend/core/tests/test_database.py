from django.db import connections
from django.db.utils import OperationalError
from django.test import TestCase


class TestDatabaseConnection(TestCase):
    def test_database_connection(self):
        """Ensure the database is accessible"""

        db_conn = connections['default']
        try:
            db_conn.ensure_connection()
        except OperationalError:
            self.fail("Database connection failed!")