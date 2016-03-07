from django.shortcuts import render, get_object_or_404

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

def {{ model.name|lower }}_detail(request, {{ model.name|lower }}_id):
    {{ model.name|lower }} = get_object_or_404({{ model.name }}.objects.select_related(), id={{ model.name|lower }}_id)
    context = {
        "{{ model.name|lower }}": {{ model.name|lower }},
    }
    return render(request, "{{ model.name|lower }}_detail.html", context)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

