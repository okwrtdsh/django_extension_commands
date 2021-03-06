import datetime
import os

import six
from django.db.models.fields.related import (
    ForeignKey, ManyToManyField, OneToOneField, RelatedField,
)
from django.template import Template, loader
from django.utils.safestring import mark_safe
from django.utils.translation import activate as activate_language

try:
    from django.utils.encoding import force_bytes
except ImportError:
    from django.utils.encoding import smart_str as force_bytes

try:
    from django.contrib.contenttypes.fields import GenericRelation
except ImportError:
    from django.contrib.contenttypes.generic import GenericRelation

from django_extension_commands.compat import get_app, get_models_compat, list_app_labels

def parse_file_or_list(arg):
    if not arg:
        return []
    if isinstance(arg, (list, tuple, set)):
        return arg
    if ',' not in arg and os.path.isfile(arg):
        return [e.strip() for e in open(arg).readlines()]
    return [e.strip() for e in arg.split(',')]


def get_app_list(app_labels, **kwargs):
    disable_fields = kwargs.get('disable_fields', False)
    include_models = parse_file_or_list(kwargs.get('include_models', ""))
    all_applications = kwargs.get('all_applications', False)
    verbose_names = kwargs.get('verbose_names', False)
    inheritance = kwargs.get('inheritance', True)
    relations_as_fields = kwargs.get("relations_as_fields", True)
    sort_fields = kwargs.get("sort_fields", False)
    language = kwargs.get('language', None)
    if language is not None:
        activate_language(language)
    exclude_columns = parse_file_or_list(kwargs.get('exclude_columns', ""))
    exclude_models = parse_file_or_list(kwargs.get('exclude_models', ""))

    def skip_field(field):
        if exclude_columns:
            if verbose_names and field.verbose_name:
                if field.verbose_name in exclude_columns:
                    return True
            if field.name in exclude_columns:
                return True
        return False

    if all_applications:
        app_labels = list_app_labels()

    app_list = []
    for app_label in app_labels:
        app = get_app(app_label)
        if not app:
            continue
        app_context = {
            'name': '"%s"' % app.__name__,
            'app_name': "%s" % '.'.join(app.__name__.split('.')[:-1]),
            'cluster_app_name': "cluster_%s" % app.__name__.replace(".", "_"),
            'models': []
        }

        appmodels = list(get_models_compat(app_label))
        abstract_models = []
        for appmodel in appmodels:
            abstract_models = abstract_models + [abstract_model for abstract_model in appmodel.__bases__ if hasattr(abstract_model, '_meta') and abstract_model._meta.abstract]
        abstract_models = list(set(abstract_models))  # remove duplicates
        appmodels = abstract_models + appmodels

        for appmodel in appmodels:
            appmodel_abstracts = [abstract_model.__name__ for abstract_model in appmodel.__bases__ if hasattr(abstract_model, '_meta') and abstract_model._meta.abstract]

            # collect all attribs of abstract superclasses
            def getBasesAbstractFields(c):
                _abstract_fields = []
                for e in c.__bases__:
                    if hasattr(e, '_meta') and e._meta.abstract:
                        _abstract_fields.extend(e._meta.fields)
                        _abstract_fields.extend(getBasesAbstractFields(e))
                return _abstract_fields
            abstract_fields = getBasesAbstractFields(appmodel)

            model = {
                'app_name': appmodel.__module__.replace(".", "_"),
                'name': appmodel.__name__,
                'abstracts': appmodel_abstracts,
                'fields': [],
                'relations': [],
                'is_abstract': True if hasattr(appmodel, '_meta') and appmodel._meta.abstract else False
            }

            # consider given model name ?
            def consider(model_name):
                if exclude_models and model_name in exclude_models:
                    return False
                elif include_models and model_name not in include_models:
                    return False
                return not include_models or model_name in include_models

            if not consider(appmodel._meta.object_name):
                continue

            if verbose_names and appmodel._meta.verbose_name:
                model['label'] = force_bytes(appmodel._meta.verbose_name)
            else:
                model['label'] = model['name']

            if appmodel._meta.verbose_name:
                model['verbose_name'] = force_bytes(appmodel._meta.verbose_name)
            else:
                model['verbose_name'] = model['name']

            # model attributes
            def add_attributes(field):
                if verbose_names and field.verbose_name:
                    label = force_bytes(field.verbose_name)
                    if label.islower():
                        label = label.capitalize()
                else:
                    label = force_bytes(field.name)

                t = type(field).__name__
                if isinstance(field, (OneToOneField, ForeignKey)):
                    t += " ({0})".format(field.rel.field_name)
                # TODO: ManyToManyField, GenericRelation

                model['fields'].append({
                    'name': field.name,
                    'label': label,
                    'type': t,
                    'blank': field.blank,
                    'abstract': field in abstract_fields,
                    'relation': isinstance(field, RelatedField),
                    'primary_key': field.primary_key,
                    'verbose_name': field.verbose_name if hasattr(field, 'verbose_name') else '',
                    'auto_now': field.auto_now if hasattr(field, 'auto_now') else False,
                    'auto_now_add': field.auto_now_add if hasattr(field, 'auto_now_add') else False,
                    'auto_created': field.auto_created if hasattr(field, 'auto_created') else False,
                    'choices': bool(getattr(field, 'choices')),
                })

            attributes = [field for field in appmodel._meta.local_fields]
            if not relations_as_fields:
                # Find all the 'real' attributes. Relations are depicted as app_context edges instead of attributes
                attributes = [field for field in attributes if not isinstance(field, RelatedField)]

            # find primary key and print it first, ignoring implicit id if other pk exists
            pk = appmodel._meta.pk
            if pk and not appmodel._meta.abstract and pk in attributes:
                add_attributes(pk)

            for field in attributes:
                if skip_field(field):
                    continue
                if pk and field == pk:
                    continue
                add_attributes(field)

            if sort_fields:
                model['fields'] = sorted(model['fields'], key=lambda field: (not field['primary_key'], not field['relation'], field['label']))

            # FIXME: actually many_to_many fields aren't saved in this model's db table, so why should we add an attribute-line for them in the resulting app_context?
            # if appmodel._meta.many_to_many:
            #    for field in appmodel._meta.many_to_many:
            #        if skip_field(field):
            #            continue
            #        add_attributes(field)

            # relations
            def add_relation(field, extras=""):
                if verbose_names and field.verbose_name:
                    label = force_bytes(field.verbose_name)
                    if label.islower():
                        label = label.capitalize()
                else:
                    label = force_bytes(field.name)

                # show related field name
                if hasattr(field, 'related_query_name'):
                    related_query_name = field.related_query_name()
                    if verbose_names and related_query_name.islower():
                        related_query_name = related_query_name.replace('_', ' ').capitalize()
                    label += force_bytes(' ({})'.format(related_query_name))

                # handle self-relationships and lazy-relationships
                if isinstance(field.rel.to, six.string_types):
                    if field.rel.to == 'self':
                        target_model = field.model
                    else:
                        raise Exception("Lazy relationship for model (%s) must be explicit for field (%s)" % (field.model.__name__, field.name))
                else:
                    target_model = field.rel.to

                _rel = {
                    'target_app': target_model.__module__.replace('.', '_'),
                    'target': target_model.__name__,
                    'type': type(field).__name__,
                    'name': field.name,
                    'label': label,
                    'arrows': extras,
                    'needs_node': True
                }
                if _rel not in model['relations'] and consider(_rel['target']):
                    model['relations'].append(_rel)

            for field in appmodel._meta.local_fields:
                if field.attname.endswith('_ptr_id'):  # excluding field redundant with inheritance relation
                    continue
                if field in abstract_fields:  # excluding fields inherited from abstract classes. they too show as local_fields
                    continue
                if skip_field(field):
                    continue
                if isinstance(field, OneToOneField):
                    add_relation(field, '[arrowhead=none, arrowtail=none, dir=both]')
                elif isinstance(field, ForeignKey):
                    add_relation(field, '[arrowhead=none, arrowtail=dot, dir=both]')

            for field in appmodel._meta.local_many_to_many:
                if skip_field(field):
                    continue
                if isinstance(field, ManyToManyField):
                    if (getattr(field, 'creates_table', False) or  # django 1.1.
                            (hasattr(field.rel.through, '_meta') and field.rel.through._meta.auto_created)):  # django 1.2
                        add_relation(field, '[arrowhead=dot arrowtail=dot, dir=both]')
                elif isinstance(field, GenericRelation):
                    add_relation(field, mark_safe('[style="dotted", arrowhead=normal, arrowtail=normal, dir=both]'))

            if inheritance:
                # add inheritance arrows
                for parent in appmodel.__bases__:
                    if hasattr(parent, "_meta"):  # parent is a model
                        l = "multi-table"
                        if parent._meta.abstract:
                            l = "abstract"
                        if appmodel._meta.proxy:
                            l = "proxy"
                        l += r"\ninheritance"
                        _rel = {
                            'target_app': parent.__module__.replace(".", "_"),
                            'target': parent.__name__,
                            'type': "inheritance",
                            'name': "inheritance",
                            'label': l,
                            'arrows': '[arrowhead=empty, arrowtail=none, dir=both]',
                            'needs_node': True,
                        }
                        # TODO: seems as if abstract models aren't part of models.getModels, which is why they are printed by this without any attributes.
                        if _rel not in model['relations'] and consider(_rel['target']):
                            model['relations'].append(_rel)

            app_context['models'].append(model)
        if app_context['models']:
            app_list.append(app_context)

    nodes = []
    for app_context in app_list:
        nodes.extend([e['name'] for e in app_context['models']])

    for app_context in app_list:
        for model in app_context['models']:
            for relation in model['relations']:
                if relation['target'] in nodes:
                    relation['needs_node'] = False

    return app_list

