import sys
from optparse import NO_DEFAULT, make_option

import six
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from django_extension_commands.management.generate_uml import generate_uml



class Command(BaseCommand):
    can_import_settings = True

    create_object_diagram_options = (
        make_option('--disable-fields', '-d', action='store_true', dest='disable_fields',
                    help='Do not show the class member fields'),
        make_option('--all-applications', '-a', action='store_true', dest='all_applications',
                    help='Automatically include all applications from INSTALLED_APPS'),
        make_option('--verbose-names', '-n', action='store_true', dest='verbose_names',
                    help='Use verbose_name of models and fields'),
        make_option('--language', '-L', action='store', dest='language',
                    help='Specify language used for verbose_name localization'),
        make_option('--exclude-columns', '-x', action='store', dest='exclude_columns',
                    help='Exclude specific column(s) from the uml. Can also load exclude list from file.'),
        make_option('--exclude-models', '-X', action='store', dest='exclude_models',
                    help='Exclude specific model(s) from the uml. Can also load exclude list from file.'),
        make_option('--include-models', '-I', action='store', dest='include_models',
                    help='Restrict the uml to specified models.'),
        make_option('--inheritance', '-e', action='store_true', dest='inheritance', default=True,
                    help='Include inheritance arrows (default)'),
        make_option('--no-inheritance', '-E', action='store_false', dest='inheritance',
                    help='Do not include inheritance arrows'),
        make_option('--hide-relations-from-fields', '-R', action='store_false', dest="relations_as_fields",
                    default=True, help="Do not show relations as fields in the uml."),
        make_option('--disable-sort-fields', '-S', action="store_false", dest="sort_fields",
                    default=True, help="Do not sort fields"),
        make_option('--gitlab_style', '-g', action="store_true", dest="gitlab_style",
                    default=False, help="Output uml for GitLab style"),
        make_option('--abstract_show', '-A', action="store_true", dest="abstract_show",
                    default=False, help="Show Abstract Model Class"),
        make_option('--package_show', '-P', action="store_true", dest="package_show",
                    default=False, help="Show Package Name"),
    )
    option_list = BaseCommand.option_list + create_object_diagram_options

    help = "Create PlantUml code for the specified app names."
    args = "[appname]"
    label = 'application name'


    def handle(self, *args, **options):
        self.options_from_settings(options)

        if len(args) < 1 and not options['all_applications']:
            raise CommandError("need one or more arguments for appname")

        cli_options = ' '.join(sys.argv[2:])
        umldata = generate_uml(args, cli_options=cli_options, **options)
        if not six.PY3:
            umldata = umldata.encode('utf-8')

        self.print_output(umldata)

    def options_from_settings(self, options):
        defaults = getattr(settings, 'CREATE_OBJECT_DIAGRAM', None)
        if defaults:
            for option in self.create_object_diagram_options:
                long_opt = option._long_opts[0]
                if long_opt:
                    long_opt = long_opt.lstrip("-").replace("-", "_")
                    if long_opt in defaults:
                        default_value = None
                        if not option.default == NO_DEFAULT:
                            default_value = option.default
                        if options[option.dest] == default_value:
                            options[option.dest] = defaults[long_opt]

    def print_output(self, umldata):
        if six.PY3 and isinstance(umldata, six.binary_type):
            umldata = umldata.decode()

        print(umldata)

