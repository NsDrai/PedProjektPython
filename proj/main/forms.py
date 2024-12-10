from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    image = forms.ImageField()

    def clean_title(self):
        title_data = self.cleaned_data['title']

        title_data = title_data.strip('!')

        if len(title_data) < 5 :
            raise ValidationError ("post title should be longer than 4 symbol")
            
        return title_data