from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Shaxar nomi')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Shaxar nomi'
        verbose_name_plural = 'Shaxarlar nomi'

    def __str__(self):
        return self.name
