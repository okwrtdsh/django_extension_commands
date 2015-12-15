# django_extension_commands


## create_object_diagram
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
![](WpDA1Vkeps3MIQZZcgdTjNrjQvsNtOXsYQIndwNNAHu3nxL3iLtujD5oR3Wc4mdIxmnZFJlMz0ORMG2Wlj5_jTADFZuFbfz9q0sAL87hSoYM1pUQGEYLVSmLPz5SvKoHwVg8eFN5YMoa)

#### for gitlab

```bash
python manage.py create_object_diagram -ag
```

```
http://utils.uci-sys.jp/plantuml?@startuml;
object LogEntry;
object Permission;
object Group;
object User;
object ContentType;
object Session;
object Staff;
object Schedule;
object OtherSchedule;
LogEntry "n" --o "1" User;
LogEntry "n" --o "1" ContentType;
Permission "n" --o "1" ContentType;
Group "n" o-o "n" Permission;
User "n" o-o "n" Group;
User "n" o-o "n" Permission;
Staff --|> User;
Schedule "n" --o "1" Staff;
LogEntry : id : AutoField;
LogEntry : content_type : ForeignKey [id];
LogEntry : user : ForeignKey [id];
LogEntry : action_flag : PositiveSmallIntegerField;
LogEntry : action_time : DateTimeField;
LogEntry : change_message : TextField;
LogEntry : object_id : TextField;
LogEntry : object_repr : CharField;
Permission : id : AutoField;
Permission : content_type : ForeignKey [id];
Permission : codename : CharField;
Permission : name : CharField;
Group : id : AutoField;
Group : name : CharField;
User : id : AutoField;
User : date_joined : DateTimeField;
User : email : EmailField;
User : first_name : CharField;
User : is_active : BooleanField;
User : is_staff : BooleanField;
User : is_superuser : BooleanField;
User : last_login : DateTimeField;
User : last_name : CharField;
User : password : CharField;
User : username : CharField;
ContentType : id : AutoField;
ContentType : app_label : CharField;
ContentType : model : CharField;
Session : session_key : CharField;
Session : expire_date : DateTimeField;
Session : session_data : TextField;
Staff : user_ptr : OneToOneField [id];
Staff : affiliation : IntegerField;
Staff : created : DateTimeField;
Staff : enabled : BooleanField;
Staff : updated : DateTimeField;
Schedule : id : AutoField;
Schedule : staff : ForeignKey [user_ptr];
Schedule : created : DateTimeField;
Schedule : date : DateField;
Schedule : enabled : BooleanField;
Schedule : end : TimeField;
Schedule : start : TimeField;
Schedule : updated : DateTimeField;
OtherSchedule : id : AutoField;
OtherSchedule : created : DateTimeField;
OtherSchedule : date : DateField;
OtherSchedule : enabled : BooleanField;
OtherSchedule : end : TimeField;
OtherSchedule : is_allday : BooleanField;
OtherSchedule : start : TimeField;
OtherSchedule : title : CharField;
OtherSchedule : updated : DateTimeField;
@enduml;
```

![](http://utils.uci-sys.jp/plantuml?@startuml;
object LogEntry;
object Permission;
object Group;
object User;
object ContentType;
object Session;
object Staff;
object Schedule;
object OtherSchedule;
LogEntry "n" --o "1" User;
LogEntry "n" --o "1" ContentType;
Permission "n" --o "1" ContentType;
Group "n" o-o "n" Permission;
User "n" o-o "n" Group;
User "n" o-o "n" Permission;
Staff --|> User;
Schedule "n" --o "1" Staff;
LogEntry : id : AutoField;
LogEntry : content_type : ForeignKey [id];
LogEntry : user : ForeignKey [id];
LogEntry : action_flag : PositiveSmallIntegerField;
LogEntry : action_time : DateTimeField;
LogEntry : change_message : TextField;
LogEntry : object_id : TextField;
LogEntry : object_repr : CharField;
Permission : id : AutoField;
Permission : content_type : ForeignKey [id];
Permission : codename : CharField;
Permission : name : CharField;
Group : id : AutoField;
Group : name : CharField;
User : id : AutoField;
User : date_joined : DateTimeField;
User : email : EmailField;
User : first_name : CharField;
User : is_active : BooleanField;
User : is_staff : BooleanField;
User : is_superuser : BooleanField;
User : last_login : DateTimeField;
User : last_name : CharField;
User : password : CharField;
User : username : CharField;
ContentType : id : AutoField;
ContentType : app_label : CharField;
ContentType : model : CharField;
Session : session_key : CharField;
Session : expire_date : DateTimeField;
Session : session_data : TextField;
Staff : user_ptr : OneToOneField [id];
Staff : affiliation : IntegerField;
Staff : created : DateTimeField;
Staff : enabled : BooleanField;
Staff : updated : DateTimeField;
Schedule : id : AutoField;
Schedule : staff : ForeignKey [user_ptr];
Schedule : created : DateTimeField;
Schedule : date : DateField;
Schedule : enabled : BooleanField;
Schedule : end : TimeField;
Schedule : start : TimeField;
Schedule : updated : DateTimeField;
OtherSchedule : id : AutoField;
OtherSchedule : created : DateTimeField;
OtherSchedule : date : DateField;
OtherSchedule : enabled : BooleanField;
OtherSchedule : end : TimeField;
OtherSchedule : is_allday : BooleanField;
OtherSchedule : start : TimeField;
OtherSchedule : title : CharField;
OtherSchedule : updated : DateTimeField;
@enduml;)
