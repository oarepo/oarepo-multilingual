import json


def get_schema():
    """This function loads the given schema available"""

    try:
        with open('test_module/jsonschemas/test/test-v1.0.0.json', 'r') as file:
            schema = json.load(file)
    except:
        with open('./tests/test_module/jsonschemas/test/test-v1.0.0.json', 'r') as file:
            schema = json.load(file)

    return schema


def test_included_pt(app):
    """Test multilingual."""
    search = app.extensions['invenio-search']
    schema = app.extensions['invenio-records']

    data = json.loads('{"title": {"cs" : "xxx","cs-en": "yyyy", "em": "jejej"}}')

    schema.validate(data, get_schema())

    assert 'test-test-v1.0.0' in search.mappings
    with open(search.mappings['test-test-v1.0.0']) as f:
        data = json.load(f)

    assert data == {
        "mappings": {
            "properties": {
                "title": {'type': 'object', 'properties':
                    {
                        'cs': {'type': 'text',
                               'fields': {
                                   "keywords": {
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
            }
        }
    }
