{% extends "django_extension_commands/template/base.tpl" %}

{% block load %}{% templatetag openblock %} load crispy_forms_tags {% templatetag closeblock %}
{% endblock %}

{% block title %}{{ model.verbose_name }}修正{% endblock %}

{% block content %}
<form action="" method="post">{% templatetag openblock %} csrf_token {% templatetag closeblock %}
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4>{{ model.verbose_name }}修正フォーム</h4>
    </div>
    <div class="panel-body">
      <table class="table table-bordered">
        {% templatetag openvariable %} form|crispy {% templatetag closevariable %}
      </table>
    </div>
    <div class="panel-footer align-center">
      <button type="submit" class="btn btn-primary">修正</button>
    </div>
  </div>
</form>{% endblock %}
