from django.shortcuts import render
from django.views import generic
from django.db import models
from movies.models import Film
from movies.models import Filmgenre
from movies.models import Actor



# Creates the titles that need to be displayed
def movies(request) :
    title = title.objects.title()
   
    context = {'title': title}

    
    return render(request,'movies/movies.html', context)

# Creates the detail view for each movie when their title is clicked on.
# Creates the film object which is used to retrieve data for display
class FilmDetailView(generic.DetailView) :
	model = Film


	def film_detail_view(self, request, filmid):

		try:

			film = Film.objects.get(pk=filmid)

		except Film.DoesNotExist:
			raise Http404('Does not exits')
		return render(request, 'movies/post.html', context={'film': film})

