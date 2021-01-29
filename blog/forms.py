from django import forms

from blog.models import Comment


class SharingByEmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ArticleSearchForm(forms.Form):
    query = forms.CharField()


