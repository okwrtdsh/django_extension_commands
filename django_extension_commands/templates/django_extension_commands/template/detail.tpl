{% extends "django_extension_commands/template/base.tpl" %}

{% block title %}{{ model.verbose_name }}詳細{% endblock %}

{% block content %}
<div class="panel panel-primary">
  <div class="panel-heading"><h4>{{ model.verbose_name }}詳細</h4></div>
  <div class="panel-body">
    <table class="table table-bordered">
      <tbody>{% for field in model.fields %}
        <tr><th>{{ field.verbose_name }}</th><td>{% templatetag openvariable %} {{ model.name|lower }}.{% if field.choices %}get_{{ field.name }}_display{% else %}{{ field.name }}{% endif %} {% templatetag closevariable %}</td></tr>{% endfor %}
      </tbody>
    </table>
  </div>
  <div class="panel-footer text-center">
    <a href="{% templatetag openblock %} url '{{ model.name|lower }}:list' {% templatetag closeblock %}"><button type="button" class="btn btn-default">戻る</button></a>
    <a href="{% templatetag openblock %} url '{{ model.name|lower }}:edit' {{ model.name|lower }}.id {% templatetag closeblock %}"><button type="button" class="btn btn-primary">修正</button></a>
  </div>
</div>{% endblock %}

