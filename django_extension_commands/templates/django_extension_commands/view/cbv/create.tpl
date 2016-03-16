{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
{% endblock %}

{% block code %}
class {{ model.name }}CreateView(SuccessMessageMixin, CreateView):
    model = {{ model.name }}
    form_class = {{ model.name }}CreateForm
    success_url = reverse_lazy('{{ model.name|lower }}:list')
    template_name = "{{ model.name|lower }}_create.html"
    success_message = '登録しました。'
{% endblock %}

