from django.views.generic.detail import DetailView

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

class {{ model.name }}DetailView(DetailView):
    model = {{ model.name }}
    template_name = "{{ model.name|lower }}_detail.html"

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

