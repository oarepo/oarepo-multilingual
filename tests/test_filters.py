import logging

import pytest
from invenio_i18n import InvenioI18N

from oarepo_multilingual import (
    language_aware_term_facet,
    language_aware_terms_filter,
    language_aware_text_match_filter,
    language_aware_text_term_facet,
    language_aware_text_terms_filter,
)


def test_no_i18n(app, caplog):
    caplog.set_level(logging.ERROR)
    with pytest.raises(KeyError):
        language_aware_text_terms_filter('blah')('a')
    assert "Exception in get_locale. Are you sure that you have added invenio_i18n to api_apps?" in caplog.text


def test_term_filter(app):
    InvenioI18N(app)

    flt = language_aware_text_terms_filter('blah')
    with app.test_request_context('/?ln=en'):
        assert flt(['a', 'b']).to_dict() == {'terms': {'blah.en.raw': ['a', 'b']}}
    with app.test_request_context('/?ln=cs'):
        assert flt(['a', 'b']).to_dict() == {'terms': {'blah.cs.raw': ['a', 'b']}}

    flt = language_aware_terms_filter('blah')
    with app.test_request_context('/?ln=en'):
        assert flt(['a', 'b']).to_dict() == {'terms': {'blah.en': ['a', 'b']}}
    with app.test_request_context('/?ln=cs'):
        assert flt(['a', 'b']).to_dict() == {'terms': {'blah.cs': ['a', 'b']}}


def test_term_facet(app):
    InvenioI18N(app)

    flt = language_aware_text_term_facet('blah')
    with app.test_request_context('/?ln=en'):
        assert flt() == {'terms': {'field': 'blah.en.raw', 'order': {'_count': 'desc'}, 'size': 100}}
    with app.test_request_context('/?ln=cs'):
        assert flt() == {'terms': {'field': 'blah.cs.raw', 'order': {'_count': 'desc'}, 'size': 100}}

    flt = language_aware_term_facet('blah')
    with app.test_request_context('/?ln=en'):
        assert flt() == {'terms': {'field': 'blah.en', 'order': {'_count': 'desc'}, 'size': 100}}
    with app.test_request_context('/?ln=cs'):
        assert flt() == {'terms': {'field': 'blah.cs', 'order': {'_count': 'desc'}, 'size': 100}}


def test_match(app):
    InvenioI18N(app)

    flt = language_aware_text_match_filter('blah')
    with app.test_request_context('/?ln=en'):
        assert flt(['a', 'b']).to_dict() == {
            'bool': {
                'minimum_should_match': 1,
                'should': [
                    {
                        'match': {
                            'blah.en': {'query': 'a'}
                        }
                    },
                    {
                        'match': {
                            'blah.en': {'query': 'b'}
                        }
                    }
                ]
            }
        }

    with app.test_request_context('/?ln=cs'):
        assert flt(['a', 'b']).to_dict() == {
            'bool': {
                'minimum_should_match': 1,
                'should': [
                    {
                        'match': {
                            'blah.cs': {'query': 'a'}
                        }
                    },
                    {
                        'match': {
                            'blah.cs': {'query': 'b'}
                        }
                    }
                ]
            }
        }
