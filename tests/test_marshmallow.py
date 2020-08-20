# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from __future__ import absolute_import, print_function

import pytest

import marshmallow
from marshmallow import ValidationError
from oarepo_multilingual.marshmallow import MultilingualStringSchemaV2


def test_marshmallow():
    """Test marshmallow."""
    class MD(marshmallow.Schema):
         title = MultilingualStringSchemaV2()

    data = {'title':
        {
            "en": "something",
            "cs-cz": "neco",
            "cs": "neco jineho"
        }
    }

    assert data == MD().load(data)

    data = {'title':
        {
            "en": "something",
            "enus": "something different"
        }
    }


    with pytest.raises(ValidationError):
        MD().load(data)

    data = {'title':
        {
            "en": "something",
            "en-us": 1
        }
    }


    with pytest.raises(ValidationError):
        MD().load(data)
