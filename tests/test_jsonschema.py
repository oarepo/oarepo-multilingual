import json
import pathlib

import jsonschema
from jsonschema import validate

# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OpenID Connect is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

def get_schema():
    """This function loads the given schema available"""
    script = False
    try:
        with open('testSchema.json', 'r') as file:
            schema = json.load(file)
    except:
        with open('./tests/testSchema.json', 'r') as file:
            schema = json.load(file)
        script = True
    if script:
        schema_url = pathlib.Path("./tests/test_json").absolute().as_uri()
    else:
        schema_url = pathlib.Path("./test_json").absolute().as_uri()
    return schema, schema_url

def validation(data, schema, base_uri):
    """This function validates given instance against given schema"""
    resolve = jsonschema.RefResolver(base_uri, base_uri)
    try:
        validate(instance=data, schema=schema, resolver =resolve)
    except:
        return False
    return True

def validationError(data, schema, base_uri):
    """This function validates given instance against given schema"""
    resolve = jsonschema.RefResolver(base_uri, base_uri)
    try:
        validate(instance=data, schema=schema, resolver =resolve)
    except:
        return True
    return False

def test_json():
    """Test for json schemas"""
    schema, schema_url = get_schema()

    data = json.loads('{"title": {"cs" : "xxx","cs-en": "yyyy", "em": "jejej"}}')
    assert validation(data, schema, schema_url)

    data2 = json.loads('{"title": {"css": "xxx"}}')
    assert validationError(data2, schema, schema_url)

    data3 = json.loads('{"title": {"cs": 1}}')
    assert validationError(data3, schema, schema_url)
