from django.urls import path
from .views import (musicapp_list,
                    musicapp_detail, musicapp_create,
                    musicapp_update, musicapp_delete,
                    navigation
                    )

app_name = 'musicapp'

urlpatterns = [
    path('', musicapp_list, name='album-list'),
    path('', navigation.as_view(), name='navigation'),
    path('<int:pk>/', musicapp_detail, name='album-detail'),
    path('<int:pk>/update/', musicapp_update, name='album-update'),
    path('<int:pk>/delete/', musicapp_delete, name='album-delete'),
    path('album_create/', musicapp_create, name='album-create')
]
