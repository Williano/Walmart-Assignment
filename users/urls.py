from django.urls import path

from .views import \
    (
     UserListView, UserDetailView, UserAlbumView,
     UserAlbumPhotosView, UserPostView, PostCommentView,
     PostDeleteView, PostUpdateView, PostUserCommentView
     )

app_name = "users"

urlpatterns = [
    path(
        route='',
        view=UserListView.as_view(),
        name='home'
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
    ),

    path(
        route='users/<int:id>/posts/',
        view=UserPostView.as_view(),
        name='user_posts'
    ),

    path(
        route='posts/<int:id>/comments/',
        view=PostCommentView.as_view(),
        name='post_comments'
    ),

    path(
        route='posts/<int:id>/delete/',
        view=PostDeleteView.as_view(),
        name='post_delete'
    ),

    path(
        route='posts/<int:id>/update/',
        view=PostUpdateView.as_view(),
        name='post_update'
    ),

    path(
        route='posts/<int:id>/user/comments/',
        view=PostUserCommentView.as_view(),
        name='post_user_comment'
    ),
]
