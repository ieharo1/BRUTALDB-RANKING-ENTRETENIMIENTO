from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    MEDIA_TYPES = [
        ('movie', 'Película'),
        ('series', 'Serie'),
        ('documentary', 'Documental'),
    ]

    name = models.CharField(max_length=180)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    year = models.PositiveIntegerField()
    duration = models.CharField(max_length=40, blank=True)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    synopsis = models.TextField()
    poster_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True)
    cast = models.ManyToManyField(Person, blank=True, related_name='titles')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', '-year', 'name']

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('title_detail', args=[self.id])


class Song(models.Model):
    title = models.CharField(max_length=180)
    artist = models.CharField(max_length=180)
    year = models.PositiveIntegerField()
    album = models.CharField(max_length=180, blank=True)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    cover_url = models.URLField(blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-score', '-year', 'title']

    def __str__(self) -> str:
        return f'{self.title} - {self.artist}'
