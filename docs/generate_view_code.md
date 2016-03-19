# generate_view_code
Viewのテンプレコードを生成するコマンド

### options
```
Usage: manage.py generate_view_code [options] [appname]

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
  -C, --class_based     Output Class Based View Format
  -T VIEW_TYPE, --view_type=VIEW_TYPE
                        Output View Type (list, create, edit, detail)
```

### Examples
```bash
python manage.py generate_view_code myapp -I MyModel -T edit
```
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def mymodel_edit(request, mymodel_id):
    mymodel = get_object_or_404(
        MyModel.objects.select_related(), id=workhistory_id)
    if request.method == "POST":
        form = MyModelEditForm(request.POST, instance=mymodel)
        if form.is_valid():
            form.save()
            messages.success(request, "修正しました。", extra_tags='alert-success')
            return redirect('mymodel:detail', mymodel_id=mymodel_id)
    else:
        form = MyModelEditForm(instance=mymodel)
    context = {
        "form": form,
    }
    return render(request, "mymodel_edit.html", context)
```

```bash
python manage.py generate_view_code myapp -I MyModel -T create -C
```

```python
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class MyModelCreateView(SuccessMessageMixin, CreateView):
    model = MyModel
    form_class = MyModelCreateForm
    success_url = reverse_lazy('mymodel:list')
    template_name = "mymodel_create.html"
    success_message = '登録しました。'
```


