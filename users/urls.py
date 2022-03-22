from django.urls import path

from .views import UserListView, UserDetailView, UserAlbumView, UserAlbumPhotosView

app_name = "users"


urlpatterns = [
    path(
        route='',
        view=UserListView.as_view(),
        name='user_list'
    ),

    path(
        route='users/<int:id>/detail',
        view=UserDetailView.as_view(),
        name='user_detail'
    ),

    path(
        route='users/<int:id>/albums/',
        view=UserAlbumView.as_view(),
        name='user_albums'
    ),

    path(
        route='albums/<int:id>/photos/',
        view=UserAlbumPhotosView.as_view(),
        name='album_photos'
    )
]
