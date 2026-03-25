from django.core.management.base import BaseCommand

from catalog.models import Person, Song, Title


class Command(BaseCommand):
    help = 'Carga datos demo estilo IMDb.'

    def handle(self, *args, **options):
        cast_data = [
            ('Christopher Nolan', 'Director'),
            ('Cillian Murphy', 'Actor'),
            ('Zendaya', 'Actriz'),
            ('Hans Zimmer', 'Compositor'),
            ('David Attenborough', 'Narrador'),
        ]
        people = {}
        for name, role in cast_data:
            person, _ = Person.objects.get_or_create(name=name, defaults={'role': role})
            people[name] = person

        titles_data = [
            {'name': 'Inception', 'media_type': 'movie', 'year': 2010, 'duration': '2h 28m', 'score': '8.8', 'synopsis': 'Un ladrón entra en sueños para robar secretos corporativos.', 'poster_url': 'https://picsum.photos/seed/inception/600/900'},
            {'name': 'Dune: Part Two', 'media_type': 'movie', 'year': 2024, 'duration': '2h 46m', 'score': '8.9', 'synopsis': 'Paul Atreides lidera la rebelión de Arrakis.', 'poster_url': 'https://picsum.photos/seed/dune/600/900'},
            {'name': 'Breaking Bad', 'media_type': 'series', 'year': 2008, 'duration': '5 temporadas', 'score': '9.5', 'synopsis': 'Un profesor de química crea un imperio criminal.', 'poster_url': 'https://picsum.photos/seed/breakingbad/600/900'},
            {'name': 'Planet Earth II', 'media_type': 'documentary', 'year': 2016, 'duration': '6 episodios', 'score': '9.4', 'synopsis': 'Documental de naturaleza con imágenes espectaculares.', 'poster_url': 'https://picsum.photos/seed/planet/600/900'},
        ]

        for item in titles_data:
            title, _ = Title.objects.get_or_create(name=item['name'], defaults=item)
            title.cast.set([people['Christopher Nolan'], people['Cillian Murphy']])

        songs_data = [
            {'title': 'Bohemian Rhapsody', 'artist': 'Queen', 'year': 1975, 'album': 'A Night at the Opera', 'score': '9.8', 'description': 'Himno rock atemporal.'},
            {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'year': 2020, 'album': 'After Hours', 'score': '9.4', 'description': 'Éxito synth-pop global.'},
            {'title': 'Billie Jean', 'artist': 'Michael Jackson', 'year': 1982, 'album': 'Thriller', 'score': '9.7', 'description': 'Clásico absoluto del pop.'},
        ]

        for song in songs_data:
            Song.objects.get_or_create(title=song['title'], artist=song['artist'], defaults=song)

        self.stdout.write(self.style.SUCCESS('Datos demo cargados correctamente.'))
