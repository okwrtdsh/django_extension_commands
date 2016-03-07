import sys
from optparse import NO_DEFAULT, make_option


import six
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from django_extension_commands.management.get_app_list import get_app_list



class CreateCodeBaseCommand(BaseCommand):
    can_import_settings = True

    create_code_options = (
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
    )
    option_list = BaseCommand.option_list + create_code_options
    help = "Create code for the specified app names."
    args = "[appname]"
    label = 'application name'

    def validate_options(self, *args, **options):
        pass

    def handle(self, *args, **options):
        self.options_from_settings(options)

        if len(args) < 1 and not options['all_applications']:
            raise CommandError("need one or more arguments for appname")
        cli_options = ' '.join(sys.argv[2:])

        self.validate_options(*args, **options)

        app_list = get_app_list(args, cli_options=cli_options, **options)
        code = self.creates_code(app_list, **options)

        if not six.PY3:
            code = code.encode('utf-8')
        self.print_output(code)

    def creates_code(self, app_list, **options):
        raise NotImplementedError

    def options_from_settings(self, options):
        defaults = getattr(settings, 'CREATE_CODE', None)
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

    def print_output(self, data):
        if six.PY3 and isinstance(data, six.binary_type):
            data = data.decode()
        print(data)

