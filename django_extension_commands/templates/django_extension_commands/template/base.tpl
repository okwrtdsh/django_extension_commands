{% for app in app_list %}{% for model_list in app %}{% if model_list.models %}{% for model in model_list.models %}{% if not model.is_abstract %}
{% templatetag opencomment %} {{ model.name }} Template {% templatetag closecomment %}
{% templatetag openblock %} extends "base.html" {% templatetag closeblock %}
{% templatetag openblock %} load static {% templatetag closeblock %}
{% block load %}{% endblock %}
{% templatetag openblock %} block title {% templatetag closeblock %}{% block title %}{% endblock %}{% templatetag openblock %} endblock {% templatetag closeblock %}

{% templatetag openblock %} block content {% templatetag closeblock %}{% block content %}{% endblock %}
{% templatetag openblock %} endblock {% templatetag closeblock %}
{% templatetag opencomment %} End {{ model.name }} Template {% templatetag closecomment %}
{% endif %}{% endfor %}{% endif %}{% endfor %}{% endfor %}
