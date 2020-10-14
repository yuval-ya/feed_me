from django.forms import ModelForm
from .models import Post

class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': '',
        }
