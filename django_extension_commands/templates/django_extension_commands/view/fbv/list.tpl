from django_pagingnavi.misc import page_context

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

def {{ model.name|lower }}_list(request):
    context = page_context(request, {{ model.name }}ListSearchForm, "{{ model.name|lower }}s", 20)
    return render(request, "{{ model.name|lower }}_list.html", context)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

