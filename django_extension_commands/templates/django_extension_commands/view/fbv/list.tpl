{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django_pagingnavi.misc import page_context
{% endblock %}

{% block code %}
def {{ model.name|lower }}_list(request):
    context = page_context(request, {{ model.name }}ListSearchForm, "{{ model.name|lower }}s", 20)
    return render(request, "{{ model.name|lower }}_list.html", context)
{% endblock %}

