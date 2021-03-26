# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Common pytest fixtures and plugins."""

from __future__ import absolute_import, print_function

import os
import shutil
import tempfile

import pytest
from flask import Flask
from flask_babelex import lazy_gettext as _
from invenio_base.signals import app_loaded
from invenio_db import InvenioDB
from invenio_indexer import InvenioIndexer
from invenio_jsonschemas import InvenioJSONSchemas
from invenio_pidstore import InvenioPIDStore
from invenio_records import InvenioRecords
from invenio_search import InvenioSearch
from oarepo_mapping_includes.ext import OARepoMappingIncludesExt
from oarepo_multilingual.ext import OARepoMultilingualExt


@pytest.yield_fixture(scope="function")
def app(request):
    """Test multilingual."""
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    app.config.update(
        ACCOUNTS_JWT_ENABLE=False,
        INDEXER_DEFAULT_DOC_TYPE='record-v1.0.0',
        RECORDS_REST_ENDPOINTS={},
        RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY=None,
        SERVER_NAME='localhost:5000',
        JSONSCHEMAS_HOST='localhost:5000',
        CELERY_ALWAYS_EAGER=True,
        CELERY_RESULT_BACKEND='cache',
        CELERY_CACHE_BACKEND='memory',
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db'
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SUPPORTED_LANGUAGES=["cs", "en"],
        BABEL_DEFAULT_LOCALE='cs',
        I18N_LANGUAGES=(
            ('en', _('English')),
        ),
        TESTING=True,
        ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE={
            "type": "text",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        }

    )

    app.secret_key = 'changeme'

    InvenioDB(app)
    InvenioRecords(app)
    InvenioJSONSchemas(app)
    InvenioPIDStore(app)
    InvenioSearch(app)
    InvenioIndexer(app)
    OARepoMappingIncludesExt(app)
    OARepoMultilingualExt(app)
    #
    app_loaded.send(app, app=app)

    with app.app_context():
        yield app

    # Teardown instance path.
    shutil.rmtree(instance_path)


@pytest.yield_fixture(scope="function")
def app_placeholder(request):
    """Test multilingual."""
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    app.config.update(
        ACCOUNTS_JWT_ENABLE=False,
        INDEXER_DEFAULT_DOC_TYPE='record-v1.0.0',
        RECORDS_REST_ENDPOINTS={},
        RECORDS_REST_DEFAULT_CREATE_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_DELETE_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_READ_PERMISSION_FACTORY=None,
        RECORDS_REST_DEFAULT_UPDATE_PERMISSION_FACTORY=None,
        SERVER_NAME='localhost:5000',
        JSONSCHEMAS_HOST='localhost:5000',
        CELERY_ALWAYS_EAGER=True,
        CELERY_RESULT_BACKEND='cache',
        CELERY_CACHE_BACKEND='memory',
        CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db'
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SUPPORTED_LANGUAGES=['cs', 'en', 'sk', 'de', 'fr', 'ru', 'es', 'nl', 'it',
                                          'no', 'pl', 'da', 'el',
                                          'hu', 'lt', 'pt', 'bg', 'ro', 'sv'],
        BABEL_DEFAULT_LOCALE='cs',
        I18N_LANGUAGES=(
            ('en', _('English')),
        ),
        TESTING=True,
        ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE={
            "type": "text",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        },
        ELASTICSEARCH_LANGUAGE_TEMPLATES={
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

    app.secret_key = 'changeme'

    InvenioDB(app)
    InvenioRecords(app)
    InvenioJSONSchemas(app)
    InvenioPIDStore(app)
    InvenioSearch(app)
    InvenioIndexer(app)
    OARepoMappingIncludesExt(app)
    OARepoMultilingualExt(app)
    #
    app_loaded.send(app, app=app)

    with app.app_context():
        yield app

    # Teardown instance path.
    shutil.rmtree(instance_path)
