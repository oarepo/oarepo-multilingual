# -*- coding: utf-8 -*- #
"""Simple test of version import."""
def handler(app,resource, json_pointer):
    """Test version import."""
    languages = app.config["SUPPORTED_LANGUAGES"]

    data_dict= dict()

    for x in languages:
        data_dict[x] = {"type" : "text",
                                               'fields': {
                                                   "keywords":{
                                                       "type": "keyword"
                                                   }
                                               }
                                         }

    return {
        "type": "object",
        "properties": data_dict
    }
