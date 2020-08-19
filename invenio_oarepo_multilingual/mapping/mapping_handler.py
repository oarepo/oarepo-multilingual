# -*- coding: utf-8 -*- #

def handler(app,resource, json_pointer):
    """Test version import."""
    languages = app.config["SUPPORTED_LANGUAGES"]

    data_dict= dict()

    for x in range(0,len(languages)):
        data_dict.update({languages[x]: {"type" : "text",
                                               'fields': {
                                                   "keywords":{
                                                       "type": "keyword"
                                                   }
                                               }
                                         }
                          }
                         )

    return {
        "type": "object",
        "properties": data_dict
    }
