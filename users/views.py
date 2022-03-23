import json

import requests

from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect


class UserListView(View):
    template_name = "users/user-list.html"
    context_object = {}

    def get(self, request):

        try:
            users = json.loads(requests.get("https://jsonplaceholder.typicode.com/users").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        user_list = [
            {"user_id": user['id'], "user_name": user["username"], "name": user["name"], "user_email": user['email']}
            for user in users]

        self.context_object['users'] = user_list

        return render(request, self.template_name, self.context_object)


class UserDetailView(View):
    template_name = "users/user-detail.html"
    context_object = {}

    def get(self, request, *arg, **kwargs):

        user_id = self.kwargs.get('id')

        try:
            user = json.loads(requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.context_object['user'] = user

        return render(request, self.template_name, self.context_object)


class UserAlbumView(View):
    template_name = "users/user-album.html"
    context_object = {}

    def get(self, request, *arg, **kwargs):

        user_id = self.kwargs.get('id')

        try:
            albums = json.loads(requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/albums/").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.context_object['albums'] = albums

        return render(request, self.template_name, self.context_object)


class UserAlbumPhotosView(View):
    template_name = "users/user-album-photos.html"
    context_object = {}

    def get(self, request, *arg, **kwargs):

        album_id = self.kwargs.get('id')

        try:
            photos = json.loads(requests.get(f"https://jsonplaceholder.typicode.com/albums/{album_id}/photos/").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.context_object['photos'] = photos

        return render(request, self.template_name, self.context_object)


class UserPostView(View):
    template_name = "users/user-post.html"
    context_object = {}

    def get(self, request, *arg, **kwargs):

        user_id = self.kwargs.get('id')

        try:
            posts = json.loads(requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts/").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.context_object['posts'] = posts

        return render(request, self.template_name, self.context_object)


class PostCommentView(View):
    template_name = "users/post-comment.html"
    context_object = {}

    def get(self, request, *arg, **kwargs):

        post_id = self.kwargs.get('id')

        try:
            comments = json.loads(requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments/").text)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        self.context_object['comments'] = comments

        return render(request, self.template_name, self.context_object)


class PostDeleteView(View):

    def post(self, request, *arg, **kwargs):

        post_id = self.kwargs.get('id')

        try:
            post = json.loads(requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}/").text)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        messages.success(request=self.request, message="Post Deleted Successfully")
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', {'users:home'}))


class PostUpdateView(View):

    def post(self, request, *arg, **kwargs):

        post_id = self.kwargs.get('id')

        updated_data = request.POST["post-update"]

        print(updated_data)

        try:
            post = requests.put(url=f"https://jsonplaceholder.typicode.com/posts/{post_id}/", data=updated_data)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        messages.success(request=self.request, message="Post Updated Successfully")
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', {'users:home'}))


class PostUserCommentView(View):

    def post(self, request, *arg, **kwargs):

        post_id = self.kwargs.get('id')

        comment = request.POST['comment-form']

        try:
            comment = requests.post(url=f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments/", data=comment)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        messages.success(request=self.request, message="Comment Added Successfully")
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', {'users:home'}))
