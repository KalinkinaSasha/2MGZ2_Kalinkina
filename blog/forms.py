
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['full_name', 'email', 'text']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше ФИО'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите email'
            }),

            'text': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Напишите ваш отзыв',
                'rows': 5
            }),
        }
