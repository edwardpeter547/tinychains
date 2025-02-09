from django import test
from django.core.management import call_command
from io import StringIO


class TestMigrations(test.TestCase):

    def test_migrations_are_applied(self):
        """Ensure that all migrations are applied"""

        out = StringIO()
        call_command("showmigrations", "--plan", stdout=out)
        output = out.getvalue()
        self.assertNotIn("[ ]", output, "Some migrations are missing!")