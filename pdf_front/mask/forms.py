from django.forms import ModelForm, forms, TextInput, PasswordInput, FileInput
from .models import Request

from django.utils.translation import gettext_lazy as _


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'author', 'password', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': "30자 이내로 입력 가능합니다."}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': "10자 이내로 입력 가능합니다."}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': "20자 이내로 입력해주세요."}),
            'content': FileInput(attrs={'class': 'form-control', 'placeholder': "이미지 혹은 영상을 업로드해주세요."}),

        }

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['maxlength'] = 30
        self.fields['author'].widget.attrs['maxlength'] = 10
        self.fields['password'].widget.attrs['maxlength'] = 20
