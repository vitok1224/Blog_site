from django import template
register = template.Library()


@register.inclusion_tag('inc/_header.html', )
def show_header():
    return


@register.inclusion_tag('inc/_footer.html', )
def show_footer():
    return
