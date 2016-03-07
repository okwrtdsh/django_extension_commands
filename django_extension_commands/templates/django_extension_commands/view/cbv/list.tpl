from django.views.generic.list import ListView

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

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

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

