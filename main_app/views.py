from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View 
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Movie



class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class MovieList(TemplateView):
    template_name = "movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["movies"] = Movie.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["movies"] = Movie.objects.all()
            context["header"] = "Trending Movies"
        return context

class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'img', 'bio', 'verified_movie']
    template_name = "movie_create.html"
    success_url = "/movies/"

class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"