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

    app.config.update(SUPPORTED_LANGUAGES = ["cs", "en"])


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
    app.config.update(SUPPORTED_LANGUAGES = [])
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
    app.config.update(SUPPORTED_LANGUAGES = ["cs"])
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
    app.config.update(SUPPORTED_LANGUAGES=["cs", "en", "_"])
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

    app.config.update(SUPPORTED_LANGUAGES=["cs", "en"])
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
    app.config.update(SUPPORTED_LANGUAGES=["en"])
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
    app.config.update(SUPPORTED_LANGUAGES=["cs"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs#kontext":
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
    assert handler(app=app, id='kontext') == {'type': 'object', 'properties':
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

    app.config.update(SUPPORTED_LANGUAGES=["cs", "en", "_"])
    app.config.update(ELASTICSEARCH_LANGUAGE_TEMPLATES={
        "cs#kontext":
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
        "_#kontext":
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
    assert handler(app=app, id='kontext') == {'type': 'object', 'properties':
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