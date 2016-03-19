# generate_template_code
Templateのテンプレコードを生成するコマンド

### options
```
Usage: manage.py generate_template_code [options] [appname]

Generate code for the specified app names.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v VERBOSITY, --verbosity=VERBOSITY
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings=SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath=PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  -d, --disable-fields  Do not show the class member fields
  -a, --all-applications
                        Automatically include all applications from
                        INSTALLED_APPS
  -n, --verbose-names   Use verbose_name of models and fields
  -L LANGUAGE, --language=LANGUAGE
                        Specify language used for verbose_name localization
  -x EXCLUDE_COLUMNS, --exclude-columns=EXCLUDE_COLUMNS
                        Exclude specific column(s) from the uml. Can also load
                        exclude list from file.
  -X EXCLUDE_MODELS, --exclude-models=EXCLUDE_MODELS
                        Exclude specific model(s) from the uml. Can also load
                        exclude list from file.
  -I INCLUDE_MODELS, --include-models=INCLUDE_MODELS
                        Restrict the uml to specified models.
  -e, --inheritance     Include inheritance arrows (default)
  -E, --no-inheritance  Do not include inheritance arrows
  -R, --hide-relations-from-fields
                        Do not show relations as fields in the uml.
  -S, --disable-sort-fields
                        Do not sort fields
  -T TEMPLATE_TYPE, --template_type=TEMPLATE_TYPE
                        Output template Type (list, create, edit, detail)
  -B, --use_beautiful_soup
                        Use BeautifulSoup
```

### Examples
```bash
python manage.py generate_template_code myapp -I MyModel -T list -B
```

```html
{# MyModel Template #}
{% extends "base.html" %}
{% load static %}
{% load pagingnavi %}

{% block title %}MyModel一覧{% endblock %}

{% block content %}
{% pagingnavi form page_obj %}
<div class="panel panel-default">
 <table class="table table-bordered table-condensed">
  <thead>
   <tr>
    <th>
     ID
    </th>
    <th>
     作成日時
    </th>
    <th>
     有効
    </th>
    <th>
     更新日時
    </th>
    <th>
     詳細
    </th>
   </tr>
  </thead>
  <tbody>
   {% for mymodel in mymodels %}
   <tr>
    <td>
     {{ mymodel.id }}
    </td>
    <td>
     {{ mymodel.created }}
    </td>
    <td>
     {{ mymodel.enabled }}
    </td>
    <td>
     {{ mymodel.updated }}
    </td>
    <td>
     <a href="{% url 'mymodel:detail' mymodel.id %}">
      <button class="btn btn-default" type="button">
       詳細
      </button>
     </a>
    </td>
   </tr>
   {% endfor %}
  </tbody>
 </table>
</div>
{% endblock %}
{# End MyModel Template #}
```

```bash
python manage.py generate_template_code myapp -I MyModel -T create
```

```html
{# MyModel Template #}
{% extends "base.html" %}
{% load static %}
{% load crispy_forms_tags %}

{% block title %}MyModel登録{% endblock %}

{% block content %}
<form action="" method="post">{% csrf_token %}
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4>MyModel登録フォーム</h4>
    </div>
    <div class="panel-body">
      <table class="table table-bordered">
        {{ form|crispy }}
      </table>
    </div>
    <div class="panel-footer align-center">
      <button type="submit" class="btn btn-primary">登録</button>
    </div>
  </div>
</form>
{% endblock %}
{# End MyModel Template #}
```

