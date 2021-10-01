from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Album


# Create your views here.


def home(request):
     all_albums = Album.objects.all()
     context={
    "all_albums":all_albums,
    }
     return render(request,'home/index.html',context)

def detail(request,album_id):
        # try:
        #     album=Album.objects.get(id=album_id)
        # except Album.DoesNotExist:
        #     raise Http404("Album does not exist")
        # # return HttpResponse("<h2>Details for Album id:" + str(album_id) +"<h2>")
        # context = {
        #     "album": album,
        # }
        album=get_object_or_404(Album,pk=album_id)
        context={"album":album}
        return render(request,'home/detail.html', context)
