from django import template
from django.conf import settings

register = template.Library()


@register.filter('fingerprinting')
def fingerprinting(key):
    if hasattr(settings, 'FINGERPRINTING') and isinstance(settings.FINGERPRINTING, dict):
        value = settings.FINGERPRINTING.get(key)
        if value:
            return value

    # By default use the standard static files logic
    return key