from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Song, Title


def home(request):
    context = {
        'top_movies': Title.objects.filter(media_type='movie')[:10],
        'top_series': Title.objects.filter(media_type='series')[:10],
        'top_documentaries': Title.objects.filter(media_type='documentary')[:10],
        'top_songs': Song.objects.all()[:10],
    }
    return render(request, 'catalog/home.html', context)


def media_list(request, media_type):
    titles = Title.objects.filter(media_type=media_type)
    labels = {
        'movie': 'Top Películas',
        'series': 'Top Series',
        'documentary': 'Top Documentales',
    }
    return render(
        request,
        'catalog/media_list.html',
        {'titles': titles, 'section_title': labels.get(media_type, 'Ranking'), 'media_type': media_type},
    )


def songs_list(request):
    return render(request, 'catalog/songs_list.html', {'songs': Song.objects.all()})


def title_detail(request, pk):
    title = get_object_or_404(Title, pk=pk)
    return render(request, 'catalog/title_detail.html', {'title': title})


def search(request):
    query = request.GET.get('q', '').strip()
    title_results = []
    song_results = []
    if query:
        title_results = Title.objects.filter(Q(name__icontains=query) | Q(synopsis__icontains=query))
        song_results = Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))

    return render(
        request,
        'catalog/search.html',
        {'query': query, 'title_results': title_results, 'song_results': song_results},
    )
