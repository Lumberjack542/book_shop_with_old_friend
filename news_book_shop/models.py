from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name='Name of News')
    description = models.TextField()

    def __str__(self):
        return self.title
