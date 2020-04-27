import base64
import uuid
from functools import partial

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class Base64ContentField(serializers.Field):
    '''
    For image , send base64 string as json
    '''

    def to_internal_value(self, data):
        try:
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            # You can save this as file instance.
            data = ContentFile(
                base64.b64decode(imgstr),
                name=str(uuid.uuid4())+'.'+ext
            )
            # print(data)
        except:
            raise ValidationError('Error in data')
        return data

    def to_representation(self, value):
        return value.url