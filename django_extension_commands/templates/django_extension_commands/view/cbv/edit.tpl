{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
{% endblock %}

{% block code %}
class {{ model.name }}EditView(SuccessMessageMixin, UpdateView):
    model = {{ model.name }}
    form_class = {{ model.name }}EditForm
    success_url = reverse_lazy('{{ model.name|lower }}:detail')
    template_name = "{{ model.name|lower }}_edit.html"
    success_message = '修正しました。'
{% endblock %}

