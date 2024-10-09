from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

class PluginApp(PluginConfig):
    default = True
    name = "pretix_email_template_plugin"
    verbose_name = "Email template helper"

    class PretixPluginMeta:
        name = gettext_lazy("Email Template")
        author = "Your name"
        description = gettext_lazy("More email template placeholders, such as {attendee_email}")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA
