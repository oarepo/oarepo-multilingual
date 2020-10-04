from invenio_i18n.selectors import get_locale
from elasticsearch_dsl import Q
import logging

log = logging.getLogger('oarepo-multilingual.rest')


def language_aware_field(fld):
    def ev():
        try:
            locale = get_locale()
        except:
            log.error('Exception in get_locale. Are you sure that you have added invenio_i18n to api_apps?')
            raise
        return f'{fld}.{locale}'

    return ev


def language_aware_text_terms_filter(field, suffix='.raw'):
    """
    provides terms filter on field.{language}.raw (the default suffix for raw subfield in text field)
    """
    field = language_aware_field(field)

    def inner(values):
        return Q('terms', **{f'{field()}{suffix}': values})

    return inner


def language_aware_terms_filter(field):
    """
    provides terms filter on field.{language} (the default suffix for raw subfield in text field)
    """
    return language_aware_text_terms_filter(field, suffix='')


def language_aware_text_match_filter(field, **kwargs):
    """
    provides fulltext match on field.{language}
    """
    field = language_aware_field(field)

    def inner(values):
        if not len(values):
            return Q('match_none')
        fld = field()
        args = {
            k: v(field=fld) if callable(v) else v for k, v in kwargs.items()
        }

        if len(values) == 1:
            return Q('match', **{
                f'{fld}': {
                    'query': values[0],
                    **args
                }
            })

        return Q('bool', should=[
            Q('match', **{
                f'{fld}': {
                    'query': val,
                    **args
                }
            }) for val in values
        ], minimum_should_match=1)

    return inner


def language_aware_text_term_facet(field, order='desc', size=100, suffix='.raw'):
    field = language_aware_field(field)

    def inner():
        return {
            'terms': {
                'field': f'{field()}{suffix}',
                'size': size,
                "order": {"_count": order}
            },
        }

    return inner


def language_aware_term_facet(field, order='desc', size=100):
    return language_aware_text_term_facet(field, order, size, suffix='')


__all__ = (
    'language_aware_field',
    'language_aware_text_terms_filter',
    'language_aware_terms_filter',
    'language_aware_text_match_filter',

    'language_aware_text_term_facet',
    'language_aware_term_facet'
)
