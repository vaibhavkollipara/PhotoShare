from django.conf.urls import url, include
from .views import (
    PhotosListApiView,
    PhotoRetrieveApiView,
    PhotoCreateApiView,
    PhotoDestroyApiView,
    UserCreateApiView,
)

app_name = "photoapi"

urlpatterns = [
    url(r'^$', include('rest_framework_docs.urls')),
    url(r'^newuser/$', UserCreateApiView.as_view(), name="new_user"),
    url(r'^photos/$', PhotosListApiView.as_view(), name="photos_list"),
    url(r'^photos/(?P<id>[0-9]+)/$', PhotoRetrieveApiView.as_view(), name="photos_retrieve"),
    url(r'^photos/add/$', PhotoCreateApiView.as_view(), name="photo_new"),
    url(r'^photos/delete/(?P<id>[0-9]+)/$', PhotoDestroyApiView.as_view(), name="photo_delete"),
]
