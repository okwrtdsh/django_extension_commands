{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django_cbv_utils.views import SearchListView
{% endblock %}

{% block code %}
class {{ model.name }}ListView(SearchListView):
    model = {{ model.name }}
    template_name = "{{ model.name|lower }}_list.html"
    context_object_name = "{{ model.name|lower }}s"
    paginate_by = 20
{% endblock %}

