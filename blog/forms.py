from django import forms
from .models import Post

# Blog Post Form

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)