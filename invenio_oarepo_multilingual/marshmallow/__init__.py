from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import SanitizedUnicode
from marshmallow.fields import List, Nested


class MultilingualStringPartSchemaV1(StrictKeysMixin):
    """Multilingual string"""

    name = SanitizedUnicode(required=True)
    lang = SanitizedUnicode(required=True)


def MultilingualStringSchemaV1():
    return Nested(MultilingualStringPartSchemaV1(), many=True)


__all__ = ('MultilingualStringSchemaV1',)
