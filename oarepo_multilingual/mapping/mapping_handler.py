# -*- coding: utf-8 -*- #
"""Simple test of version import."""
def handler(type=None, resource=None, id=None, json_pointer=None,
            app=None, content=None, root=None, content_pointer=None):
    """Use this function as handler."""
    languages = app.config.get("SUPPORTED_LANGUAGES", [])
    default_template = app.config.get("ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE", {})
    template = app.config.get("ELASTICSEARCH_LANGUAGE_TEMPLATES", {})

    data_dict= dict()
    for x in languages:
        if id is not None:
            y = x + '#' + id
            if y in template.keys():
                data_dict[x] = template[y]
            elif x in template.keys():
                data_dict[x] = template[x]
            else:
                data_dict[x] = default_template
        elif x in template.keys():
            data_dict[x] = template[x]
        else:
            data_dict[x] = default_template


    return {
        "type": "object",
        "properties": data_dict
    }
