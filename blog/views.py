from django.shortcuts import render

# Blog Views

def post_list(request):
	return render(request, 'blog/post_list.html', {})

