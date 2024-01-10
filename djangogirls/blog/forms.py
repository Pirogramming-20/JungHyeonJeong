from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    # 이 폼을 만들기 위해 어떤 model이 사용되어야 하는지 알려주는 구문
    class Meta:
        model = Post
        fields = ('title', 'text',)