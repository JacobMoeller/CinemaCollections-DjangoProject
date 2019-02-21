from django.contrib import admin
from movies.models import Film,Actor,Director,Producer,Genre

# Register your models here.
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(Genre)
