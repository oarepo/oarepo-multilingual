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
    app.config = {
            "SUPPORTED_LANGUAGES": ["cs", "en"]
    }

    print(app.config["SUPPORTED_LANGUAGES"])
    assert ["cs", "en"] == app.config["SUPPORTED_LANGUAGES"]

    assert handler(app) == {'type': 'object', 'properties':
                                        {
                                        'cs': {'type': 'text',
                                               'fields': {
                                                   "keywords":{
                                                       "type": "keyword"
                                                   }
                                               }},
                                        'en': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }
                                               }
                                        }
                                      }
    app.config = {
        "SUPPORTED_LANGUAGES": []
    }
    assert handler(app) == {'type': 'object', 'properties':
                                                                    {
                                                                    }
                                      }
    app.config = {"SUPPORTED_LANGUAGES": ["cs"]}
    assert handler(app) == {'type': 'object', 'properties':
        {
            'cs': {'type': 'text',
                   'fields': {
                       "keywords": {
                           "type": "keyword"
                       }
                   }}
        }
                                      }
