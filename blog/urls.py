from django.conf.urls import url
from . import views

# Blog - URL Routes

urlpatterns = [
	url(r'^$', views.post_list),
]

