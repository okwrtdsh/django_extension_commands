# generate_form_code
Formのテンプレコードを生成するコマンド

### options
```
Usage: manage.py generate_form_code [options] [appname]

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
  -T FORM_TYPE, --form_type=FORM_TYPE
                        Output Form Type (list, create, edit)

```

### Examples
```bash
python manage.py generate_form_code myapp -I MyModel -T list
```
```python
from django import forms
from django_cbv_utils.forms import SearchForm


class MyModelListSearchForm(SearchForm):

    class Meta:
        model = MyModel
        fields = [
            'id',
            'created',
            'enabled',
            'updated',
        ]

    queryset_filter = {
        "id": {
            "flds": ["id"]},
        "created": {
            "op": "date",
            "flds": ["created"]},
        "enabled": {
            "flds": ["enabled"]},
        "updated": {
            "op": "date",
            "flds": ["updated"]},
    }

    created = forms.DateField(label="作成日時")
    enabled = forms.TypedChoiceField(label="有効", choices=(
        ("", "---------"), (True, "はい"), (False, "いいえ")), coerce=lambda x: x == "True", empty_value=None)
    updated = forms.DateField(label="更新日時")
```

```bash
python manage.py generate_form_code myapp -I MyModel -T create
```

```python
from django import forms


class MyModelCreateForm(forms.ModelForm):

    class Meta:
        model = MyModel
        fields = [
            'created',
            'enabled',
            'updated',
        ]
```

