from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

class {{ model.name }}CreateView(CreateView):
    model = {{ model.name }}
    form_class = {{ model.name }}CreateForm
    success_url = reverse_lazy('{{ model.name|lower }}:list')
    template_name = "{{ model.name|lower }}_create.html"

    def form_valid(self, form):
        messages.success(self.request, "登録しました。", extra_tags="alert-success")
        return super({{ model.name }}CreateView, self).form_valid(form)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

