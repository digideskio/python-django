from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post  				# . means current directory or current application
from .forms import PostForm
from django.shortcuts import redirect

# Blog Views

'''
	Views are supposed to do: connect models and templates. In our post_list view we will need
	to take models we want to display and pass them to the template. So basically in a view we 
	decide what (model) will be displayed in a template.

'''

def post_list(request):
	#if Post.objects.count() != 0: 
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'blog/post_list.html', {'posts' : posts})
	#else:
		#return render(request, 'blog/post_list.html', {'posts' : None})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})




