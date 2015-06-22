from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post  				# . means current directory or current application

# Blog Views

'''
	Views are supposed to do: connect models and templates. In our post_list view we will need
	to take models we want to display and pass them to the template. So basically in a view we 
	decide what (model) will be displayed in a template.

'''

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
