# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Simple test of version import."""

from __future__ import absolute_import, print_function

import marshmallow
import pytest
from marshmallow import ValidationError

from invenio_oarepo_multilingual.marshmallow import MultilingualStringSchemaV2


def test_marshmallow():
    """Test version import."""
    class MD(marshmallow.Schema):
         title = MultilingualStringSchemaV2()

    data = {'title':
        {
            "en": "something",
            "cs-cz": "neco",
            "cs": "neco jineho"
        }
    }

    if marshmallow.__version_info__[0] == 2:
        # marshmallow 2
        assert data == MD().load(data).data
    else:
        assert data == MD().load(data)

    data = {'title':
        {
            "en": "something",
            "enus": "something different"
        }
    }

    if marshmallow.__version_info__[0] == 2:
             # marshmallow 2
        print(MD().load(data))
        assert MD().load(data).errors == {'title': ['Invalid type.']}
    else:
        with pytest.raises(ValidationError):
            MD().load(data)

    data = {'title':
        {
            "en": "something",
            "en-us": 1
        }
    }

    if marshmallow.__version_info__[0] == 2:
        # marshmallow 2
        print(MD().load(data))
        assert MD().load(data).errors == {'title': ['Invalid type.']}
    else:
        with pytest.raises(ValidationError):
            MD().load(data)
