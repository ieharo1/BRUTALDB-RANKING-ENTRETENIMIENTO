from django.contrib import admin

from .models import Person, Song, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'media_type', 'year', 'score')
    list_filter = ('media_type', 'year')
    search_fields = ('name', 'synopsis')
    filter_horizontal = ('cast',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year', 'score')
    list_filter = ('year',)
    search_fields = ('title', 'artist', 'description')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
