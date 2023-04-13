import json

from django.core.serializers.json import DjangoJSONEncoder


def class_serialize(obj):
    # ----------------------------------------------------------------------------
    # note to remember ===> not "serializable"
    # class instance serialization error solved
    # b_dict = b_data.__dict__
    # b_dict.pop('_state', None)  # removes not json serializable object from dict
    # b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)  # Now it's ok
    # ----------------------------------------------------------------------------
    b_dict = obj.__dict__
    b_dict.pop('_state', None)
    b_serialized = json.dumps(b_dict, cls=DjangoJSONEncoder)

    return b_serialized
