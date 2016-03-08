{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.views.generic.detail import DetailView
{% endblock %}

{% block code %}
class {{ model.name }}DetailView(DetailView):
    model = {{ model.name }}
    template_name = "{{ model.name|lower }}_detail.html"
{% endblock %}

