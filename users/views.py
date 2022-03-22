import json

import requests

from django.shortcuts import render
from django.views import View


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
