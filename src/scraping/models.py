from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Shaxar nomi',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Shaxar nomi'
        verbose_name_plural = 'Shaxarlar nomi'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Dasturlash tili',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Dasturlash tili'
        verbose_name_plural = 'Dasturlash tillari'

    def __str__(self):
        return self.name
