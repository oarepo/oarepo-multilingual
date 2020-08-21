# -*- coding: utf-8 -*- #
"""Simple test of version import."""
def handler(type=None, resource=None, id=None, json_pointer=None,
            app=None, content=None, root=None, content_pointer=None):
    """Use this function as handler."""
    try:
        languages = app.config["SUPPORTED_LANGUAGES"]
    except:
        languages = list()
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
