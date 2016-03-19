{% extends "django_extension_commands/form/base.tpl" %}

{% block import %}
from django import forms
{% endblock %}

{% block code %}
class {{ model.name }}CreateForm(forms.ModelForm):
    class Meta:
        model = {{ model.name }}
        fields = [{% for field in model.fields %}{% if not field.auto_now and not field.auto_now_add and not field.auto_created %}
            '{{ field.name }}',{% endif %}{% endfor %}
        ]
{% endblock %}

