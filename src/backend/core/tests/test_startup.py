from django.test import SimpleTestCase
from django.conf import settings


class TestTalkspaceStartup(SimpleTestCase):

    def test_app_settings_loaded(self):
        """Ensure Django settings are properly loaded"""

        self.assertTrue(settings.SECRET_KEY, "SECRET_KEY is missing!")
        self.assertTrue(settings.INSTALLED_APPS, "INSTALLED_APPS is empty!")

    def test_default_installed_apps(self):
        """Ensure essential default apps are installed"""

        essential_apps = [
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "rest_framework",
            "shared"
        ]
        for app in essential_apps:
            self.assertIn(app, settings.INSTALLED_APPS, f"{app} is missing in INSTALLED_APPS")