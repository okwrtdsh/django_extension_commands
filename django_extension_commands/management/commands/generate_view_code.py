import sys
from optparse import NO_DEFAULT, make_option

import autopep8

from django.core.management.base import CommandError
from django.template import Context, Template, loader

from django_extension_commands.management.generate_code_base import GenerateCodeBaseCommand


class Command(GenerateCodeBaseCommand):

    generate_view_code_options = (
        make_option('--class_based', '-C', action="store_true", dest="class_based",
            default=False, help="Output Class Based View Format"),
        make_option('--view_type', '-T', action="store", dest="view_type",
            default=None,
            help="Output View Type (list, create, edit, detail)"),
    )
    option_list = GenerateCodeBaseCommand.option_list +\
        generate_view_code_options


    def validate_options(self, *args, **options):
        self.class_based = options.get("class_based", False)
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
                'cbv' if self.class_based else 'fbv',
                self.view_type
            ))
        if not isinstance(t, Template) and not (hasattr(t, 'template') and isinstance(t.template, Template)):
            raise Exception("Default Django template loader isn't used. "
                            "This can lead to the incorrect template rendering. "
                            "Please, check the settings.")

        c = Context({
            'app_list': app_list,
        })
        code = t.render(c)
        code = autopep8.fix_code(code)
        return code

