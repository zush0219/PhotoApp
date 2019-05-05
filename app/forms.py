from django.forms import ModelForm
from .models import Photo, Icon


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'comment', 'image', 'category']


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = ['image']