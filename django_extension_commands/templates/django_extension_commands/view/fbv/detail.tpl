{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.shortcuts import render, get_object_or_404
{% endblock %}

{% block code %}
def {{ model.name|lower }}_detail(request, {{ model.name|lower }}_id):
    {{ model.name|lower }} = get_object_or_404({{ model.name }}.objects.select_related(), id={{ model.name|lower }}_id)
    context = {
        "{{ model.name|lower }}": {{ model.name|lower }},
    }
    return render(request, "{{ model.name|lower }}_detail.html", context)
{% endblock %}

