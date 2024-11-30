from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя:')
    email = forms.EmailField(label='Ваш aдрес электронной почты')
    message = forms.CharField(widget=forms.Textarea, label='Ваше сообщение')


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя:')
    email = forms.EmailField(label='Ваш aдрес электронной почты')
    feedback = forms.CharField(widget=forms.Textarea, label='Ваш отзыв')
