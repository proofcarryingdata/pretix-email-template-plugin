# Register your receivers here
from django.dispatch import receiver
from pretix.base.email import BaseMailTextPlaceholder
from pretix.base.signals import register_text_placeholders
from pretix.base.services.placeholders import SimpleFunctionalTextPlaceholder


def get_best_email(position_or_address):
    from pretix.base.models import InvoiceAddress, OrderPosition
    if isinstance(position_or_address, InvoiceAddress):
        return position_or_address.order.email
    if isinstance(position_or_address, OrderPosition):
        if position_or_address.attendee_email:
            return position_or_address.attendee_email
        else:
            return position_or_address.order.email

class AttendeeOrOrderEmailPlaceholder(BaseMailTextPlaceholder):
    def __init__(self):
        self._identifier = "email"

    @property
    def required_context(self):
        return ["position_or_address"]

    @property
    def identifier(self):
        return self._identifier

    def render(self, context):
        position_or_address = context["position_or_address"]
        return get_best_email(position_or_address)

    def render_sample(self, context):
        return "richard@0xparc.org"


@receiver(register_text_placeholders, dispatch_uid="placeholder_email")
def register_placeholder_renderers(sender, **kwargs):
    return AttendeeOrOrderEmailPlaceholder()
