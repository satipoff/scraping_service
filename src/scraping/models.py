from django.db import models

# Create your models here.
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Shaxar nomi',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Shaxar nomi'
        verbose_name_plural = 'Shaxarlar nomi'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))

        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Dasturlash tili',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Dasturlash tili'
        verbose_name_plural = 'Dasturlash tillari'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))

        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name="Vakansiya sarlavqasi")
    company = models.CharField(max_length=250, verbose_name="Kampaniya")
    description = models.TextField(verbose_name="Vakansiya tavsifi")
    city = models.ForeignKey('city', on_delete=models.CASCADE, verbose_name="Shahar")
    language = models.ForeignKey('language', on_delete=models.CASCADE, verbose_name="Dasturlash tili")
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'

    def __str__(self):
        return self.title
