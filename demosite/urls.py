from django.conf.urls import include, url, patterns
from django.contrib import admin

'''
	Basic REGEX commands for URL Pattern matching:

	r indicates that a regular expression follows
	^ for beginning of the text
	$ for end of text
	\d for a digit
	+ to indicate that the previous item should be repeated at least once
	() to capture part of the pattern

'''

urlpatterns = [
    # Examples:
    # url(r'^$', 'demosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'', include('blog.urls')),
]


'''
Extended comments concerning url definitions using REGEX commands:

Now imagine you have a website with the address like that: http://www.mysite.com/post/12345/, 
where 12345 is the number of your post.

Writing separate views for all the post numbers would be really annoying. With regular expression 
we can create a pattern that will match the url and extract the number for us: ^post/(\d+)/$ 

Let's break it down piece by piece to see what we are doing here:

    ^post/ is telling Django to take anything that has post/ at the beginning of the url (right after ^)
    (\d+) means that there will be a number (one or more digits) and that we want the number captured and extracted
    / tells django that another / character should follow
    $ then indicates the end of the URL meaning that only strings ending with the / will match this pattern

'''