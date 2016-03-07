from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

class {{ model.name }}EditView(UpdateView):
    model = {{ model.name }}
    form_class = {{ model.name }}EditForm
    success_url = reverse_lazy('{{ model.name|lower }}:detail')
    template_name = "{{ model.name|lower }}_edit.html"

    def form_valid(self, form):
        messages.success(self.request, "修正しました。", extra_tags="alert-success")
        return super({{ model.name }}EditView, self).form_valid(form)

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

