{% extends "django_extension_commands/template/base.tpl" %}

{% block load %}{% templatetag openblock %} load pagingnavi {% templatetag closeblock %}
{% endblock %}

{% block title %}{{ model.verbose_name }}一覧{% endblock %}

{% block content %}
{% templatetag openblock %} pagingnavi form page_obj {% templatetag closeblock %}
<div class="panel panel-default">
  <table class="table table-bordered table-condensed">
    <thead>
      <tr>
        {% for field in model.fields %}<th>{{ field.verbose_name }}</th>{% endfor %}<th>詳細</th>
      </tr>
    </thead>
    <tbody>
      {% templatetag openblock %} for {{ model.name|lower }} in {{ model.name|lower }}s {% templatetag closeblock %}
      <tr>
        {% for field in model.fields %}<td>{% templatetag openvariable %} {{ model.name|lower }}.{% if field.choices %}get_{{ field.name }}_display{% else %}{{ field.name }}{% endif %} {% templatetag closevariable %}</td>{% endfor %}<td><a href="{% templatetag openblock %} url '{{ model.name|lower }}:detail' {{ model.name|lower }}.id {% templatetag closeblock %}"><button type="button" class="btn btn-default">詳細</button></a></td>
      </tr>
      {% templatetag openblock %} endfor {% templatetag closeblock %}
    </tbody>
  </table>
</div>{% endblock %}
