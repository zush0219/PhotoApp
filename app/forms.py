from django.forms import ModelForm
from .models import Photo, Icon, Comment


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'category']


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = ['image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']