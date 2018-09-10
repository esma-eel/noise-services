from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=500)
    email = forms.EmailField()
    phone = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea()) 
    file = forms.FileField()

    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'شماره تماس'})
    message.widget.attrs.update({'class': 'form-control', 'placeholder': 'پیام'})
    file.widget.attrs.update({'class': 'form-control', 'placeholder': 'ارسال فایل', 'accept':
        ".pdf, .docx, .jpg, .png", 'draggable':"true"})

    class Meta:
        model = Contact

        fields = [
            'name',
            'email',
            'phone',
            'message',
            'file',
        ]