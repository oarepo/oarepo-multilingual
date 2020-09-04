from oarepo_multilingual import config

class OARepoMultilingualExt:
    def __init__(self, app, db=None):
        self.init_app(app, db=None)

    def init_app(self, app, db=None):
        self.init_config(app)

    def init_config(self, app):
        app.config.setdefault(
            'ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE',
            config.ELASTICSEARCH_DEFAULT_LANGUAGE_TEMPLATE
        )
