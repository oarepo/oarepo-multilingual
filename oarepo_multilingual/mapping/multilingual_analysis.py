# -*- coding: utf-8 -*- #
"""Handler for multilingual analyzer."""
def multilingual_analysis(type=None, resource=None, id=None, json_pointer=None,
            app=None, content=None, root=None, content_pointer=None):
    """Use this function as handler."""
    languages = app.config.get("SUPPORTED_LANGUAGES", [])

    analyzer= app.config.get("ELASTICSEARCH_LANGUAGE_ANALYSIS", {})

    analysis_list = list()

    for l in languages:
        if id is not None:
            x = l + '#' + id
            if x in analyzer.keys():
                analysis_list.append(analyzer[x])
        if l in analyzer.keys():
            analysis_list.append(analyzer[l])

    result = {}
    for l in analysis_list:
        result.update(l)
    return {
        "analyzer": result
    }






