from django import template

register = template.Library()

@register.filter
def status_badge(value):
    if value == 'open':
        return "bg-warning text-dark"
    elif value == 'pending':
        return "bg-info"
    elif value == 'answered':
        return "bg-success"
    else:
        return "bg-secondary"

@register.filter
def priority_badge(value):
    if value == 'low':
        return "bg-success"
    elif value == 'normal':
        return "bg-primary"
    elif value == 'high':
        return "bg-warning text-dark"
    else:
        return "bg-danger"
