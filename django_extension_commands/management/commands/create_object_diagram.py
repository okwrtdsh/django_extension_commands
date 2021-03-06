from django.template import Template, loader
from django_extension_commands.management.generate_code_base import GenerateCodeBaseCommand


class Command(GenerateCodeBaseCommand):

    help = "Create PlantUml code for the specified app names."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--gitlab_style', '-g', action="store_true", dest="gitlab_style",
                            default=False, help="Output uml for GitLab style"),
        parser.add_argument('--abstract_show', '-A', action="store_true", dest="abstract_show",
                            default=False, help="Show Abstract Model Class"),
        parser.add_argument('--package_show', '-P', action="store_true", dest="package_show",
                            default=False, help="Show Package Name"),

    def validate_options(self, *args, **options):
        self.gitlab_style = options.get("gitlab_style", False)
        self.abstract_show = options.get("abstract_show", False)
        self.package_show = options.get("package_show", False)

    def generate_code(self, app_list, **options):
        if self.gitlab_style:
            t = loader.get_template('django_extension_commands/uml/gitlab.uml')
        else:
            t = loader.get_template('django_extension_commands/uml/default.uml')

        if not isinstance(t, Template) and not (hasattr(t, 'template') and isinstance(t.template, Template)):
            raise Exception("Default Django template loader isn't used. "
                            "This can lead to the incorrect template rendering. "
                            "Please, check the settings.")

        # unique
        model_list = []
        for app_context in app_list:
            for model in app_context['models']:
                if model not in model_list:
                    model_list.append(model)

        c = {
            'disable_fields': options.get('disable_fields', False),
            'model_list': model_list,
            'abstract_show': self.abstract_show,
            'package_show': self.package_show,
        }
        uml = t.render(c)

        if self.gitlab_style:
            uml = uml.replace("(", "[").replace(")", "]")
        return uml

