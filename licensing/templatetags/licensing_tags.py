from django import template
from django.template import Context, loader
import logging


register = template.Library()

@register.inclusion_tag('licensing/setup.html')
def licensing_style(klass='openwebicon'):
    '''Usage:

        {% licensing_style 'foobar' %}

    Render a <style> block with the (optional) class
    '''
    return {
        'class': klass,
    }

@register.simple_tag(takes_context=True)
def show_license(context, license_instance, template='licensing/symbols.html'):
    '''
    Usage:

        {% show_license license template="path/to/template" %}

    The template argument can be omitted, a default template is included.
    '''
    ctx = {
        'symbols': license_instance.symbols,
    }

    t = context.template.engine.get_template(template) if hasattr(context, 'template') else loader.get_template(template)

    return t.render(Context(ctx))
