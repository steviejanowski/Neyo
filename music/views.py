
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.db.models import Q
from .models import Album, Song
from .forms import UserForm





def index(request):
    all_albums=Album.objects.order_by('-pub_date')

    # all_albums.order_by('-pub_date')
    return render(request, 'music/index.html', {'all_albums':all_albums})

# class IndexView(generic.ListView):
#     template_name = 'music/index.html'
#     context_object_name = 'all_albums'
#     def get_queryset(self):
#         return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields=['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields=['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class =UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.if_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})


def travel(request):
    all_albums = Album.objects.filter(genre="Rock")

    # all_albums.order_by('-pub_date')
    return render(request, 'music/travel.html', {'all_albums': all_albums})


def software(request):
    all_albums = Album.objects.filter(genre="Jazz")

    # all_albums.order_by('-pub_date')
    return render(request, 'music/travel.html', {'all_albums': all_albums})


def mind(request):
    all_albums = Album.objects.filter(genre="Modern")

    # all_albums.order_by('-pub_date')
    return render(request, 'music/travel.html', {'all_albums': all_albums})



