{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.views.generic.list import ListView
{% endblock %}

{% block code %}
class {{ model.name }}ListView(ListView):
    model = {{ model.name }}
    template_name = "{{ model.name|lower }}_list.html"
    context_object_name = "{{ model.name|lower }}s"
    paginate_by = 20

    def get_queryset(self):
        return {{ model.name }}ListSearchForm(self.request.GET).get_queryset()

    def get_context_data(self, **kwargs):
        context = super({{ model.name }}ListView, self).get_context_data(**kwargs)
        context["form"] = {{ model.name }}ListSearchForm(self.request.GET)
        return context
{% endblock %}

