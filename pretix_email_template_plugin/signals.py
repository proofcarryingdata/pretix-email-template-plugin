# Register your receivers here
from django.dispatch import receiver
from pretix.base.email import BaseMailTextPlaceholder
from pretix.base.signals import register_text_placeholders


class AttendeeEmailPlaceholder(BaseMailTextPlaceholder):
    def __init__(self):
        self._identifier = "attendee_email"

    @property
    def required_context(self):
        return ["order", "position"]

    @property
    def identifier(self):
        return self._identifier

    def render(self, context):
        position = context["position"]
        return position.attendee_email

    def render_sample(self, context):
        return "richard@0xparc.org"


@receiver(register_text_placeholders, dispatch_uid="placeholder_custom")
def register_placeholder_renderers(sender, **kwargs):
    return AttendeeEmailPlaceholder()
