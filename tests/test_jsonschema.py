import json
import traceback
import jsonschema
import pathlib

from jsonschema import validate

def get_schema():
    """This function loads the given schema available"""

    with open('./test.json', 'r') as file:
        schema = json.load(file)
    schema_url = pathlib.Path("./test_json").absolute().as_uri()
    return schema, schema_url

def validation(data, schema, base_uri):
    resolve = jsonschema.RefResolver(base_uri, base_uri)
    try:
        validate(instance=data, schema=schema, resolver =resolve)
    except:
        return False
    return True

def validationError(data, schema, base_uri):
    resolve = jsonschema.RefResolver(base_uri, base_uri)
    try:
        validate(instance=data, schema=schema, resolver =resolve)
    except:
        return True
    return False

def test_json():

    schema, schema_url = get_schema()

    data = json.loads('{"title": {"cs" : "xxx","cs-en": "yyyy", "em": "jejej"}}')
    assert validation(data, schema, schema_url)

    data2 = json.loads('{"title": {"css": "xxx"}}')
    assert validationError(data2, schema, schema_url)

    data3 = json.loads('{"title": {"cs": 1}}')
    assert validationError(data3, schema, schema_url)