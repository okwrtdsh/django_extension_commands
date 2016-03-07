from django.shortcuts import render, redirect
from django.contrib import messages

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

def {{ model.name|lower }}_create(request):
    if request.method == "POST":
        form = {{ model.name }}CreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "登録しました。", extra_tags='alert-success')
            return redirect('{{ model.name|lower }}:list')
    else:
        form = {{ model.name }}CreateForm()
    context = {
        'form': form,
    }
    return render(request, '{{ model.name|lower }}_create.html', context)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

