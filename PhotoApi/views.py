from .serializers import (
    PhotoSerializer,
    PhotoListSerializer,
    UserSerializer
)
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    CreateAPIView
)
from .models import Photo
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsPhotoOwner
from .pagination import MyPageNumberPagination


class PhotosListApiView(ListAPIView):
    """
    Endpoint to view photos list
    """
    serializer_class = PhotoListSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPageNumberPagination
    queryset = Photo.objects.all()


class PhotoCreateApiView(CreateAPIView):
    """
    Endpoint to upload new photo
    """
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        owner = self.request.user
        photo = self.request.data['photo']
        serializer.save(owner=owner, photo=photo)


class PhotoDestroyApiView(DestroyAPIView):
    """
    Endpoint to delete photo
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, IsPhotoOwner]
    lookup_url_kwarg = 'id'
    queryset = Photo.objects.all()


class UserCreateApiView(CreateAPIView):
    """
    Endpoint to register new user
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
