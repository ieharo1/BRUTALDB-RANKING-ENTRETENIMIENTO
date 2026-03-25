from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top/peliculas/', views.media_list, {'media_type': 'movie'}, name='movies_list'),
    path('top/series/', views.media_list, {'media_type': 'series'}, name='series_list'),
    path('top/documentales/', views.media_list, {'media_type': 'documentary'}, name='documentaries_list'),
    path('top/canciones/', views.songs_list, name='songs_list'),
    path('titulo/<int:pk>/', views.title_detail, name='title_detail'),
    path('buscar/', views.search, name='search'),
]
