# Allows the admin, and those with access to create blog posts for the site

from django.contrib import admin
from blog.models import Post

admin.site.register(Post)
