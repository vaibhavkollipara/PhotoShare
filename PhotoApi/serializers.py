from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    Serializer
)
from django.contrib.auth.models import User

from .models import Photo


class PhotoListSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'uploaded_by',
            'id',
            'image_src',
            'upload_date'
        ]


class PhotoSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'photo'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username)
        user_obj.set_password(password)
        try:
            user_obj.save()
        except:
            raise APIException("Problem creating account !Try again with different details")
        return validated_data
