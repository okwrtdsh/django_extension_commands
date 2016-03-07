# django_extension_commands


## [create_object_diagram](./doc/create_object_diagram.md)
ER図(PlantUml)を自動生成するコマンド

### options
```
Usage: manage.py create_object_diagram [options] [appname]

Create PlantUml code for the specified app names.

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
  -g, --gitlab_style    Output uml for GitLab style
  -A, --abstract_show   Show Abstract Model Class
  -P, --package_show    Show Package Name
```

### Examples
#### default
```bash
python manage.py create_object_diagram -a
```

```
@startuml
object LogEntry
object Permission
object Group
object User
object ContentType
object Session
object Staff
object Schedule
object OtherSchedule
LogEntry "n" --o "1" User
LogEntry "n" --o "1" ContentType
Permission "n" --o "1" ContentType
Group "n" o-o "n" Permission
User "n" o-o "n" Group
User "n" o-o "n" Permission
Staff --|> User
Schedule "n" --o "1" Staff
LogEntry : id : AutoField
LogEntry : content_type : ForeignKey (id)
LogEntry : user : ForeignKey (id)
LogEntry : action_flag : PositiveSmallIntegerField
LogEntry : action_time : DateTimeField
LogEntry : change_message : TextField
LogEntry : object_id : TextField
LogEntry : object_repr : CharField
Permission : id : AutoField
Permission : content_type : ForeignKey (id)
Permission : codename : CharField
Permission : name : CharField
Group : id : AutoField
Group : name : CharField
User : id : AutoField
User : date_joined : DateTimeField
User : email : EmailField
User : first_name : CharField
User : is_active : BooleanField
User : is_staff : BooleanField
User : is_superuser : BooleanField
User : last_login : DateTimeField
User : last_name : CharField
User : password : CharField
User : username : CharField
ContentType : id : AutoField
ContentType : app_label : CharField
ContentType : model : CharField
Session : session_key : CharField
Session : expire_date : DateTimeField
Session : session_data : TextField
Staff : user_ptr : OneToOneField (id)
Staff : affiliation : IntegerField
Staff : created : DateTimeField
Staff : enabled : BooleanField
Staff : updated : DateTimeField
Schedule : id : AutoField
Schedule : staff : ForeignKey (user_ptr)
Schedule : created : DateTimeField
Schedule : date : DateField
Schedule : enabled : BooleanField
Schedule : end : TimeField
Schedule : start : TimeField
Schedule : updated : DateTimeField
OtherSchedule : id : AutoField
OtherSchedule : created : DateTimeField
OtherSchedule : date : DateField
OtherSchedule : enabled : BooleanField
OtherSchedule : end : TimeField
OtherSchedule : is_allday : BooleanField
OtherSchedule : start : TimeField
OtherSchedule : title : CharField
OtherSchedule : updated : DateTimeField
@enduml
```
![](http://plantuml.com:80/plantuml/png/XLN1RjmW4BttAwmzDOSSUksXKficLPL8YRIRCsBjMIyf1WlZD9RwyHt0EE0ncujjU0_clPa1w-CBrBPwqEsjicRwfCFu2KmdXa5e5MT-6JtsSV0yW8dVDrfPKFOmzH2dzf0jtLj-EYs3-WpDA1Vkeps3MIQZZcgdTjNrjQvsNtOXsYQIndwNNAHu3nxL3iLtujD5oR3Wc4mdIxmnZFJlMz0ORMG2Wlj5_jTADFZuFbfz9q0sAL87hSoYM1pUQGEYLVSmLPz5SvKoHwVg8eFN5YMoa-GjZfxq8AnuXNt7fVoDKLem9Foyn8hEHV_9BHpmaweySzK2wx38l7NC0xnPmWhbPTxi9OA1tZcvEVDPK597agiC-o1RAsu3YdjVXKW43Sr29CHfmdyE9LdHvza6aybUj53GaDJE5EYuaFY-TUyCEGapM5OCE31Nk5S7_j1Q0bThVF1zMeR77ipSKLiKoJ6yrArG9UsUKHBOys7ugqspXRceP5roP6b2Sv3tFPFy2FB21XtMFiVd-mddXl35_i1KOC1RBmmmLq3Ydkw3D9ur_7vElJFAUkiyFoeuQ7nuGkZLoCAda8BRi6bsJYEbDe0QQ1T57DlyA3sUbNBHqJVRo-FLHHAU8B6FqgCMZLsbnAB8TqgIK8ALFAGCVwziROmYZIs19VlPNuZcO0sN_ArvnEIQK71AQRbT8XVl02aRFdsq4KtEcc65bVbnN3CAEVmF)
