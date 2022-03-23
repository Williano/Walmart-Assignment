from django.urls import path

from .views import \
    (
     UserListView, UserDetailView, UserAlbumView,
     UserAlbumPhotosView, UserPostView, PostCommentView,
     PostDeleteView, PostUpdateView, PostUserCommentView
     )

app_name = "users"

urlpatterns = [

    # Home
    path(
        route='',
        view=UserListView.as_view(),
        name='home'
    ),

    # User Detail
    path(
        route='users/<int:id>/detail',
        view=UserDetailView.as_view(),
        name='user_detail'
    ),

    # User Albums
    path(
        route='users/<int:id>/albums/',
        view=UserAlbumView.as_view(),
        name='user_albums'
    ),

    # User Photos
    path(
        route='albums/<int:id>/photos/',
        view=UserAlbumPhotosView.as_view(),
        name='album_photos'
    ),

    # User Posts
    path(
        route='users/<int:id>/posts/',
        view=UserPostView.as_view(),
        name='user_posts'
    ),

    # User Post Comments
    path(
        route='posts/<int:id>/comments/',
        view=PostCommentView.as_view(),
        name='post_comments'
    ),

    # User Post Delete
    path(
        route='posts/<int:id>/delete/',
        view=PostDeleteView.as_view(),
        name='post_delete'
    ),

    # User Post Update
    path(
        route='posts/<int:id>/update/',
        view=PostUpdateView.as_view(),
        name='post_update'
    ),

    # User Comment on Post
    path(
        route='posts/<int:id>/user/comments/',
        view=PostUserCommentView.as_view(),
        name='post_user_comment'
    ),
]
