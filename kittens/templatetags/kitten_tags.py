from django import template
register = template.Library()
@register.filter
def whatsapp_link(kitten, phone_number):
    return kitten.whatsapp_link(phone_number)
