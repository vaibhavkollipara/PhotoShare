from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Photo(models.Model):

    photo = models.ImageField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Photo by user {}".format(self.owner)

    @property
    def uploaded_by(self):
        return self.owner.username

    class Meta:
        db_table = 'photos'
        ordering = ['-upload_date']
        verbose_name = "photo"
        verbose_name_plural = "photos"
