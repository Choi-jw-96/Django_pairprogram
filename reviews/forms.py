from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        label='content', 
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width : 500px',
            'placeholder' : '댓글을 써주세요'
        }
        )
    )
