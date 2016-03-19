import sys
from optparse import NO_DEFAULT, make_option

from bs4 import BeautifulSoup

from django.core.management.base import CommandError
from django.template import Context, Template, loader

from django_extension_commands.management.generate_code_base import GenerateCodeBaseCommand


class Command(GenerateCodeBaseCommand):

    generate_template_code_options = (
        make_option('--template_type', '-T', action="store", dest="template_type",
            default=None,
            help="Output template Type (list, create, edit, detail)"),
        make_option('--use_beautiful_soup', '-B', action="store_true", dest="use_beautiful_soup",
            default=False, help="Use BeautifulSoup"),
    )
    option_list = GenerateCodeBaseCommand.option_list +\
        generate_template_code_options


    def validate_options(self, *args, **options):
        self.use_beautiful_soup = options.get("use_beautiful_soup", False)
        template_type = options.get("template_type")
        if template_type is None:
            raise CommandError("Need --template_type option.")
        if template_type.lower() in ('list', 'create', 'edit', 'detail'):
            self.template_type = template_type
        else:
            raise CommandError(
                "Need --template_type option. Choose one from (list, create, edit, detail).")


    def generate_code(self, app_list, **options):
        t = loader.get_template(
            'django_extension_commands/template/{0}.tpl'.format(
                self.template_type
            ))
        if not isinstance(t, Template) and not (hasattr(t, 'template') and isinstance(t.template, Template)):
            raise Exception("Default Django template loader isn't used. "
                            "This can lead to the incorrect template rendering. "
                            "Please, check the settings.")

        c = Context({
            'app_list': app_list,
        })
        code = t.render(c)
        if self.use_beautiful_soup:
            code = BeautifulSoup(code, "html.parser").prettify()
        return code

