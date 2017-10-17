from django.contrib import admin
from .models import Photo


class PhotoAdminModel(admin.ModelAdmin):
    list_display = ['id', 'owner', 'upload_date']
    list_filter = ['owner', 'upload_date']


admin.site.register(Photo, PhotoAdminModel)
