{% extends "django_extension_commands/form/base.tpl" %}

{% block import %}
from django import forms
from django_cbv_utils.forms import SearchForm
{% endblock %}

{% block code %}
class {{ model.name }}ListSearchForm(SearchForm):
    class Meta:
        model = {{ model.name }}
        fields = [{% for field in model.fields %}
            '{{ field.name }}',{% endfor %}
        ]

    queryset_filter = [{% for field in model.fields %}{% if not field.auto_created or not field.relation %}{% if field.type == 'DateTimeField' %}
        {"targets": "{{ field.name }}", "op": "date",
         "fields": "{{ field.name }}"},{% else %}
        {"targets": "{{ field.name }}", "fields": "{{ field.name }}"},{% endif %}{% endif %}{% endfor %}
    ]

{% for field in model.fields %}{% if not field.auto_created or not field.relation %}{% if field.type == 'DateTimeField' %}    {{ field.name }} = forms.DateField(label="{{ field.verbose_name }}")
{% endif %}{% if field.type == 'BooleanField' %}    {{ field.name }} = forms.TypedChoiceField(label="{{ field.verbose_name }}", choices=(("", "---------"), (True, "はい"), (False, "いいえ")), coerce=lambda x: x == "True", empty_value=None)
{% endif %}{% if field.type in char_fields %}    {{ field.name }} = forms.CharField(label="{{ field.verbose_name }}")
{% endif %}{% endif %}{% endfor %}
{% endblock %}

