{% block import %}
{% endblock %}

{% for app in app_list %}
{% for model_list in app %}
{% if model_list.models %}
{% for model in model_list.models %}
{% if not model.is_abstract %}

{% block code %}
{% endblock %}

{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

