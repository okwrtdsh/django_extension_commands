import sys
from optparse import NO_DEFAULT, make_option


import six
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from django_extension_commands.management.get_app_list import get_app_list



class GenerateCodeBaseCommand(BaseCommand):
    can_import_settings = True

    help = "Generate code for the specified app names."
    args = "[appname]"
    label = 'application name'

    def add_arguments(self, parser):
        parser.add_argument('--disable-fields', '-d', action='store_true', dest='disable_fields',
                            help='Do not show the class member fields'),
        parser.add_argument('--all-applications', '-a', action='store_true', dest='all_applications',
                            help='Automatically include all applications from INSTALLED_APPS'),
        parser.add_argument('--verbose-names', '-n', action='store_true', dest='verbose_names',
                            help='Use verbose_name of models and fields'),
        parser.add_argument('--language', '-L', action='store', dest='language',
                            help='Specify language used for verbose_name localization'),
        parser.add_argument('--exclude-columns', '-x', action='store', dest='exclude_columns',
                            help='Exclude specific column(s) from the uml. Can also load exclude list from file.'),
        parser.add_argument('--exclude-models', '-X', action='store', dest='exclude_models',
                            help='Exclude specific model(s) from the uml. Can also load exclude list from file.'),
        parser.add_argument('--include-models', '-I', action='store', dest='include_models',
                            help='Restrict the uml to specified models.'),
        parser.add_argument('--inheritance', '-e', action='store_true', dest='inheritance', default=True,
                            help='Include inheritance arrows (default)'),
        parser.add_argument('--no-inheritance', '-E', action='store_false', dest='inheritance',
                            help='Do not include inheritance arrows'),
        parser.add_argument('--hide-relations-from-fields', '-R', action='store_false', dest="relations_as_fields",
                            default=True, help="Do not show relations as fields in the uml."),
        parser.add_argument('--sort-fields', '-S', action="store_true", dest="sort_fields",
                            default=False, help="Sort fields"),

    def validate_options(self, *args, **options):
        pass

    def handle(self, *args, **options):
        if len(args) < 1 and not options['all_applications']:
            raise CommandError("need one or more arguments for appname")
        cli_options = ' '.join(sys.argv[2:])

        self.validate_options(*args, **options)

        app_list = get_app_list(args, cli_options=cli_options, **options)
        code = self.generate_code(app_list, **options)

        if not six.PY3:
            code = code.encode('utf-8')
        self.print_output(code)

    def generate_code(self, app_list, **options):
        raise NotImplementedError

    def print_output(self, data):
        if six.PY3 and isinstance(data, six.binary_type):
            data = data.decode()
        print(data)


