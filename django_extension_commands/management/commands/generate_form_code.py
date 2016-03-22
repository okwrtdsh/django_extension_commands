import sys
from optparse import NO_DEFAULT, make_option

import autopep8

from django.core.management.base import CommandError
from django.template import Context, Template, loader

from django_extension_commands.management.generate_code_base import GenerateCodeBaseCommand


class Command(GenerateCodeBaseCommand):

    generate_form_code_options = (
        make_option('--form_type', '-T', action="store", dest="form_type",
            default=None,
            help="Output Form Type (list, create, edit)"),
    )
    option_list = GenerateCodeBaseCommand.option_list +\
        generate_form_code_options


    def validate_options(self, *args, **options):
        form_type = options.get("form_type")
        if form_type is None:
            raise CommandError("Need --form_type option.")
        if form_type.lower() in ('list', 'create', 'edit'):
            self.form_type = form_type
        else:
            raise CommandError(
                "Need --form_type option. Choose one from (list, create, edit).")


    def generate_code(self, app_list, **options):
        t = loader.get_template(
            'django_extension_commands/form/{0}.tpl'.format(
                self.form_type
            ))
        if not isinstance(t, Template) and not (hasattr(t, 'template') and isinstance(t.template, Template)):
            raise Exception("Default Django template loader isn't used. "
                            "This can lead to the incorrect template rendering. "
                            "Please, check the settings.")

        c = Context({
            'app_list': app_list,
            'char_fields': [
                "SlugField",
                "URLField",
                "EmailField",
                "FileField",
                "IPAddressField",
            ]
        })
        code = t.render(c)
        code = autopep8.fix_code(code)
        return code

