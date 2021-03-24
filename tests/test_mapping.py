# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from flask import Flask

from oarepo_multilingual.mapping.mapping_handler import handler


def test_mapping():
    """Simple test of mapping."""
    app = Flask('testapp')
    app.config.update(ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE={
        "type": "text",
        "fields": {
            "raw": {
                "type": "keyword"
            }
        }
    })

    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "en", "_"])

    assert handler(app=app) == {
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
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["_"])
    assert handler(app=app) == {
        'type': 'object', 'properties':
            {
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
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "_"])
    assert handler(app=app) == {
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
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "en", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "text"
                }
            }
        },
        "en": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "text"
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
    )

    assert handler(app=app) == {
        'type': 'object', 'properties':
            {
                'cs': {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "text"
                        }
                    }
                },
                'en': {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "text"
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

    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "en", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "text"
                }
            }
        }
    }
    )

    assert handler(app=app) == {
        'type': 'object', 'properties':
            {
                'cs': {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "text"
                        }
                    }
                },
                'en': {
                    "type": "text",
                    "fields": {
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
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["en", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "_": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "text"
                }
            }
        }
    }
    )

    assert handler(app=app) == {
        'type': 'object', 'properties':
            {
                'en': {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                '_': {
                    'type': 'text',
                    'fields': {
                        "raw": {
                            "type": "text"
                        }
                    }
                }
            }
    }


def test_ids():
    app = Flask('testapp')
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs#context":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "text"
                    },
                    "jej":
                        {"type": "text"}
                }
            },
        "cs":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "text"
                    }
                }
            }

    }
    )
    assert handler(app=app, id='context') == {
        'type': 'object', 'properties':
            {
                'cs': {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "text"
                        },
                        "jej": {"type": "text"}
                    }
                },
                '_': {}

            }
    }

    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES=["cs", "en", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs#context":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "text"
                    },
                    "jej":
                        {"type": "text"}
                }
            },
        "cs":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    }

                }
            },
        "en":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    }
                }
            },
        "_#context":
            {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "text"
                    }
                }
            }

    }
    )
    assert handler(app=app, id='context') == {
        'type': 'object', 'properties':
            {
                'cs': {
                    'type': 'text',
                    'fields': {
                        "raw": {
                            "type": "text"
                        },
                        "jej":
                            {"type": "text"}
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
                            "type": "text"
                        }
                    }
                }
            }
    }


def test_all_languages():
    app = Flask('testapp')
    app.config.update(
        MULTILINGUAL_SUPPORTED_LANGUAGES=['cs', 'en', 'sk', 'de', 'fr', 'ru', 'es', 'nl', 'it',
                                          'no', 'pl', 'da', 'el',
                                          'hu', 'lt', 'pt', 'bg', 'ro', 'sv'])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
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
    assert handler(app=app, id='context') == {
        'properties': {
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


def test_all_languages_2():
    app = Flask('testapp')
    app.config.update(
        MULTILINGUAL_SUPPORTED_LANGUAGES=['cs', 'en', 'sk', 'de', 'fr', 'ru', 'es', 'nl', 'it',
                                          'no', 'pl', 'da', 'el',
                                          'hu', 'lt', 'pt', 'bg', 'ro', 'sv'])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "*#context": {
            "type": "text",
            "copy_to": "field",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        }

    }
    )
    assert handler(app=app, id='context') == {
        'properties': {
            'bg': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'cs': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'da': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'de': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'el': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'en': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'es': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'fr': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'hu': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'it': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'lt': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'nl': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'no': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'pl': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'pt': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'ro': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'ru': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'sk': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            },
            'sv': {
                'copy_to': 'field',
                'fields': {'raw': {'type': 'keyword'}},
                'type': 'text'
            }
        },
        'type': 'object'
    }
