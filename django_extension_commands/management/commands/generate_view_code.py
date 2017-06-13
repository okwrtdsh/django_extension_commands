import sys
from optparse import NO_DEFAULT, make_option

import autopep8

from django.core.management.base import CommandError
from django.template import Template, loader

from django_extension_commands.management.generate_code_base import GenerateCodeBaseCommand


class Command(GenerateCodeBaseCommand):

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--function_based', '-F', action="store_true",
                            dest="function_based",
                            default=False, help="Output Class Based View Format"),
        parser.add_argument('--view_type', '-T', action="store", dest="view_type",
                            default=None,
                            help="Output View Type (list, create, edit, detail)"),


    def validate_options(self, *args, **options):
        self.function_based = options.get("function_based", False)
        view_type = options.get("view_type")
        if view_type is None:
            raise CommandError("Need --view_type option.")
        if view_type.lower() in ('list', 'create', 'edit', 'detail'):
            self.view_type = view_type
        else:
            raise CommandError(
                "Need --view_type option. Choose one from (list, create, edit, detail).")


    def generate_code(self, app_list, **options):
        t = loader.get_template(
            'django_extension_commands/view/{0}/{1}.tpl'.format(
                'fbv' if self.function_based else 'cbv',
                self.view_type
            ))
        if not isinstance(t, Template) and not (hasattr(t, 'template') and isinstance(t.template, Template)):
            raise Exception("Default Django template loader isn't used. "
                            "This can lead to the incorrect template rendering. "
                            "Please, check the settings.")

        c = {
            'app_list': app_list,
        }
        code = t.render(c)
        code = autopep8.fix_code(code)
        return code

