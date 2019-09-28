from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video', 'cover')


class VideoEditForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ('title', 'description', 'tags', 'categories')