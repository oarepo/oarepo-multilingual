from flask import Flask

from oarepo_multilingual.mapping.multilingual_analysis import multilingual_analyzer


def test_analyzer():
    """Test of multilingual analyzer"""
    app2 = Flask('testapp')
    app2.config = {"ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }}}}

    assert multilingual_analyzer(app=app2) == {'analyzer': {}
        }

    app2 = Flask('testapp')
    app2.config = {"SUPPORTED_LANGUAGES": ["cs"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }}}}


    assert multilingual_analyzer(app=app2) == {
        "analyzer": {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }
    }}
    app2.config = {"SUPPORTED_LANGUAGES": ["cs", "en"],"ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
        }
    }

    assert multilingual_analyzer(app=app2) == {
        "analyzer": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }
    }

    app2.config = {"SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
        }}

    assert multilingual_analyzer(app=app2) == {
        "analyzer": {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }
    }

    app2.config = {"SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
    }
                   }

    assert multilingual_analyzer(app=app2) == {
        "analyzer": {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }
    }

    app2.config = {"SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs#title": {"czech#title": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard"
    }},
        "cs": {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
    }
                   }

    assert multilingual_analyzer(app=app2, id='title') == {
        "analyzer": {"czech#title": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard"
        },
            "czech": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }
    }
