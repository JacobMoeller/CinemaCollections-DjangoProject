from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from movies.models import Film
from movies.models import Actor
from movies.views import movies
from django.urls import re_path
from django.urls import path
from movies import views
from movies.views import FilmDetailView

# The first path creates URLs out of every movie title, and the second path maps their directories with their
# respective primary key and is formatted via the post.html file.
urlpatterns = [path('', ListView.as_view(queryset=Film.objects.all(),
                                         template_name="movies/movies.html")),

               path('<int:pk>', FilmDetailView.as_view(model=Film,template_name="movies/post.html")), 
                                         
              
]

