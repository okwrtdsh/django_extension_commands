{% extends "django_extension_commands/view/base.tpl" %}

{% block import %}
from django.shortcuts import render, redirect
from django.contrib import messages
{% endblock %}

{% block code %}
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
{% endblock %}

