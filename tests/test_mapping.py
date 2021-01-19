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
    app.config.update( ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE={
            "type": "text",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        })

    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES = ["cs", "en", "_"])

    assert handler(app=app) == {'type': 'object', 'properties':
        {
            'cs': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "keyword"
                       }
                   }},
            'en': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "keyword"
                       }
                   }
                   },
            '_': {'type': 'text',
                               'fields': {
        "raw": {
            "type": "keyword"
        }
    }
    }
        }
                               }
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES = ["_"])
    assert handler(app=app) == {'type': 'object', 'properties':
        {
                                '_': {'type': 'text',
                                      'fields': {
                                          "raw": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
        }
                                }
    app.config.update(MULTILINGUAL_SUPPORTED_LANGUAGES = ["cs", "_"])
    assert handler(app=app) == {'type': 'object', 'properties':
        {
            'cs': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "keyword"
                       }
                   }},
            '_': {'type': 'text',
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
            '_': {'type': 'text',
                               'fields': {
        "raw": {
            "type": "keyword"
        }
    }
    }
    }
    )

    assert handler(app=app) == {'type': 'object', 'properties':
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
                                '_': {'type': 'text',
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

    assert handler(app=app) == {'type': 'object', 'properties':
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
            '_': {'type': 'text',
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

    assert handler(app=app) == {'type': 'object', 'properties':
        {
            'en': {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "keyword"
                    }
                }
            },
            '_': {'type': 'text',
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
    assert handler(app=app, id='context') == {'type': 'object', 'properties':
        {
            'cs': {
                "type": "text",
                "fields": {
                    "raw": {
                        "type": "text"
                    },
                    "jej": {"type":"text"}
                }
            },
            '_': {}


                     }}

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
    assert handler(app=app, id='context') == {'type': 'object', 'properties':
        {
            'cs': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "text"
                       },
                    "jej":
                        {"type": "text"}
                   }},
            'en': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "keyword"
                       }
                   }
                   },
            '_': {'type': 'text',
                   'fields': {
                       "raw": {
                           "type": "text"
                       }
                   }
                   }
        }
                               }