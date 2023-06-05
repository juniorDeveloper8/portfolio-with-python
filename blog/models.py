import datetime
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    url = models.DateField(datetime.date.today)
