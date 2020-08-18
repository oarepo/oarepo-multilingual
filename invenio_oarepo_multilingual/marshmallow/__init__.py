"""Support for multilingual strings in oarepo invenio repository."""

from marshmallow.fields import List, Nested
from marshmallow import Schema, INCLUDE, fields, validate, RAISE, post_load, validates_schema, ValidationError
import re

# class DictField(fields.Field):
#
#     def __init__(self, key_field, nested_field, *args, **kwargs):
#         fields.Field.__init__(self, *args, **kwargs)
#         self.key_field = key_field
#         self.nested_field = nested_field
#
#     def _deserialize(self, value, **kwargs):
#         ret = {}
#         for key, val in value.items():
#             k = self.key_field.deserialize(key)
#             v = self.nested_field.deserialize(val)
#             ret[k] = v
#         return ret
#
#     def _serialize(self, value, attr, obj):
#         ret = {}
#         for key, val in value.items():
#             k = self.key_field._serialize(key, attr, obj)
#             v = self.nested_field.serialize(key, self.get_value(attr, obj))
#             ret[k] = v
#         return ret

class MultilingualStringPartSchemaV2(Schema):

    @validates_schema
    def validate_schema(self, data, **kwargs):
        errors = {}
        list_data = list(data)
        for s in list_data:
            if not re.match('^[a-z][a-z]$', s) and not re.match('^[a-z][a-z]-[a-z][a-z]$',s):
                raise ValidationError("Wrong language name")
            if not isinstance((data[s]),str):
                raise ValidationError("Wrong data type")

        # for s in list_data:
        #     if not ((re.match('^[a-z][a-z]$', s)) and isinstance(data[s], str)):
        #         raise ValidationError("Wrong data")
        #     elif not ( (re.match('^[a-z][a-z]-[a-z][a-z]$', s)) and isinstance(data[s], str)):
        #         raise ValidationError("Wrong data")

    # @post_load
    # def keys_validation(self, item, many, **kwargs):
    #     item['email'] = item['email'].lower().strip()
    #     return item
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
    #return Nested(DictField(fields.Str(validate=validate.Regexp(r'^[a-z][a-z]$')), fields.Str()), many=True, *kwargs)
    return Nested(MultilingualStringPartSchemaV2(),  **kwargs)
    #return Nested(fields.Str(validate=validate.Regexp(r'^[a-z][a-z]$')), fields.Str())
    #return DictField(fields.Str(validate=validate.Regexp(r'^[a-z][a-z]$')), fields.Str())



__all__ = ('MultilingualStringSchemaV2')
