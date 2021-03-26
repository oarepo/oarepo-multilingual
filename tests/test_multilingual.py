import json


def get_schema(file_name='test-v1.0.0.json'):
    """This function loads the given schema available"""

    try:
        with open('test_module/jsonschemas/test/%s' % file_name, 'r') as file:
            schema = json.load(file)
    except:
        with open('./tests/test_module/jsonschemas/test/%s' % file_name, 'r') as file:
            schema = json.load(file)

    return schema


def test_included_pt(app):
    """Test multilingual."""
    search = app.extensions['invenio-search']
    schema = app.extensions['invenio-records']

    data = json.loads('{"title": {"cs" : "xxx","cs-en": "yyyy", "em": "jejej"}}')

    schema.validate(data, get_schema())

    assert 'test-test-v1.0.0' in search.mappings
    with open(search.mappings['test-test-v1.0.0']) as f:
        data = json.load(f)

    assert data == {
        "mappings": {
            "properties": {
                "title": {
                    'type': 'object', 'properties':
                        {
                            'cs': {
                                'type': 'text',
                                'fields': {
                                    "raw": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            'en': {
                                'type': 'text',
                                'fields': {
                                    "raw": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            '_': {
                                'type': 'text',
                                'fields': {
                                    "raw": {
                                        "type": "keyword"
                                    }
                                }
                            }
                        }
                }
            }
        }
    }


def test_placeholder(app_placeholder):
    from invenio_base.signals import app_loaded
    """Test multilingual."""
    app_placeholder.config.update(
        MULTILINGUAL_SUPPORTED_LANGUAGES=['cs', 'en', 'sk', 'de', 'fr', 'ru', 'es', 'nl', 'it',
                                          'no', 'pl', 'da', 'el',
                                          'hu', 'lt', 'pt', 'bg', 'ro', 'sv'])
    app_placeholder.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "*#context": {
            "type": "text",
            "copy_to": "field.*",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        }

    }
    )

    search = app_placeholder.extensions['invenio-search']
    schema = app_placeholder.extensions['invenio-records']

    data = json.loads('{"title": {"cs" : "xxx","cs-en": "yyyy", "em": "jejej"}}')

    crr_schema = get_schema()
    schema.validate(data, crr_schema)

    assert 'test-test-v2.0.0' in search.mappings
    with open(search.mappings['test-test-v2.0.0']) as f:
        data = json.load(f)

    assert data == {
        'mappings': {
            'properties': {
                'title': {
                    'properties': {
                        '_': {
                            'copy_to': 'field._',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'bg': {
                            'copy_to': 'field.bg',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'cs': {
                            'copy_to': 'field.cs',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'da': {
                            'copy_to': 'field.da',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'de': {
                            'copy_to': 'field.de',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'el': {
                            'copy_to': 'field.el',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'en': {
                            'copy_to': 'field.en',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'es': {
                            'copy_to': 'field.es',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'fr': {
                            'copy_to': 'field.fr',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'hu': {
                            'copy_to': 'field.hu',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'it': {
                            'copy_to': 'field.it',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'lt': {
                            'copy_to': 'field.lt',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'nl': {
                            'copy_to': 'field.nl',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'no': {
                            'copy_to': 'field.no',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pl': {
                            'copy_to': 'field.pl',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'pt': {
                            'copy_to': 'field.pt',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ro': {
                            'copy_to': 'field.ro',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'ru': {
                            'copy_to': 'field.ru',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sk': {
                            'copy_to': 'field.sk',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        },
                        'sv': {
                            'copy_to': 'field.sv',
                            'fields': {'raw': {'type': 'keyword'}},
                            'type': 'text'
                        }
                    },
                    'type': 'object'
                }
            }
        }
    }
