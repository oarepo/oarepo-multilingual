"""Support for multilingual strings in oarepo invenio repository."""

from marshmallow.fields import List, Nested
from marshmallow import Schema, INCLUDE, fields, validate, RAISE, post_load, validates_schema, ValidationError
import re

class MultilingualStringPartSchemaV2(Schema):

    @validates_schema
    def validate_schema(self, data, **kwargs):
        list_data = list(data)
        for s in list_data:
            if not re.match('^[a-z][a-z]$', s) and not re.match('^[a-z][a-z]-[a-z][a-z]$',s):
                raise ValidationError("Wrong language name")
            if not isinstance((data[s]),str):
                raise ValidationError("Wrong data type")

    class Meta:
        unknown = INCLUDE

class MultilingualStringPartSchemaV1(Schema):
    """Multilingual string."""

    value = fields.Str(required=True)
    lang = fields.Str(required=True)

    class Meta:
        unknown = RAISE


def MultilingualStringSchemaV1(**kwargs):
    """Return a schema for multilingual string."""
    return Nested(MultilingualStringPartSchemaV1(many=True), many=True,  **kwargs)

def MultilingualStringSchemaV2(**kwargs):
    """Return a schema for multilingual string."""
    return Nested(MultilingualStringPartSchemaV2(),  **kwargs)

__all__ = ('MultilingualStringSchemaV2')
