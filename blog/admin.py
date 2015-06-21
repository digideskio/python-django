from django.contrib import admin
from .models import Post			# We import the Post model defined in the Blog app

# Registering Blog and Django admin

admin.site.register(Post)	
