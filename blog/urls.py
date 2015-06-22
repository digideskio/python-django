from django.conf.urls import url
from . import views

# Blog - URL Routes

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]

'''
	
	For views.post_detail:

		-  it starts with ^ again -- "the beginning"
    	-  post/ only means that after the beginning, the URL should contain the word post and /. So far so good.
    	-  (?P<pk>[0-9]+) - this part is trickier. It means that Django will take everything that you place here
    			and transfer it to a view as a variable called pk.
    			[0-9] also tells us that it can only be a number, not a letter (so everything between 0 and 9). 
    			+ means that there needs to be one or more digits there. 
    			So something like http://127.0.0.1:8000/post// is not valid, 
    			but http://127.0.0.1:8000/post/1234567890/ is perfectly ok!
    	-  / - then we need / again
    	-  $ - "the end"!

That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are 
looking for a view called post_detail and transfer the information that pk equals 5 to that view.

pk is shortcut for primary key. This name is often used in Django projects. But you can name your variable 
as you like (remember: lowercase and _ instead of whitespaces!).

For example instead of (?P<pk>[0-9]+) we could have variable post_id, so this bit would look like: (?P<post_id>[0-9]+)

'''