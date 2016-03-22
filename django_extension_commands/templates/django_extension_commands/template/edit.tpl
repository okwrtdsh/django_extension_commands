{% extends "django_extension_commands/template/base.tpl" %}

{% block title %}{{ model.verbose_name }}修正{% endblock %}

{% block content %}
<form action="" method="post">{% templatetag openblock %} csrf_token {% templatetag closeblock %}
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4>{{ model.verbose_name }}修正フォーム</h4>
    </div>
    <div class="panel-body">
      <table class="table table-bordered">
        <tbody>{% for field in model.fields %}{% if not field.auto_now and not field.auto_now_add and not field.auto_created %}
          <tr {% templatetag openblock %} if form.{{ field.name }}.errors {% templatetag closeblock %}class="alert-danger"{% templatetag openblock %} endif {% templatetag closeblock %}>
            <th>{% templatetag openvariable %} form.{{ field.name }}.label {% templatetag closevariable %}</th>
            <td>{% templatetag openvariable %} form.{{ field.name }}.errors {% templatetag closevariable %}{% templatetag openvariable %} form.{{ field.name }} {% templatetag closevariable %}</td>
          </tr>{% endif %}{% endfor %}
        <tbody>
      </table>
    </div>
    <div class="panel-footer text-center">
      <button type="submit" class="btn btn-primary">修正</button>
    </div>
  </div>
</form>{% endblock %}
