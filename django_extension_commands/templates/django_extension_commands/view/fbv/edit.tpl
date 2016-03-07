from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

def {{ model.name|lower }}_edit(request, {{ model.name|lower }}_id):
    {{ model.name|lower }} = get_object_or_404({{ model.name }}.objects.select_related(), id={{ model.name|lower }}_id)
    if request.method == "POST":
        form = {{ model.name }}EditForm(request.POST, instance={{ model.name|lower }})
        if form.is_valid():
            form.save()
            messages.success(request, "修正しました。", extra_tags='alert-success')
            return redirect('{{ model.name|lower }}:detail', {{ model.name|lower }}_id={{ model.name|lower }}_id)
    else:
        form = {{ model.name }}EditForm(instance={{ model.name|lower }})
    context = {
        "form": form,
    }
    return render(request, "{{ model.name|lower }}_edit.html", context)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

