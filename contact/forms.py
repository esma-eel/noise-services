from django import forms
from .models import Contact
# from pricing.models import PricePlan


# choices_plan = [('هیچکدام','هیچکدام'),]
# for price in PricePlan.objects.all():
#     choices_plan.append((price.name, price.name))


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=500)
    email = forms.EmailField()
    phone = forms.IntegerField()
    # which_price_plan = forms.ChoiceField(choices=choices_plan, widget=forms.Select())
    message = forms.CharField(widget=forms.Textarea()) 
    file = forms.FileField(required=False)


    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'شماره تماس'})
    # which_price_plan.widget.attrs.update({'class': 'form-control', 'placeholder': 'کدام تعرفه را انتخاب کردید ؟'})
    message.widget.attrs.update({'class': 'form-control', 'placeholder': 'متن پیام یا سفارش'})
    file.widget.attrs.update({'class': 'form-control', 'placeholder': 'ارسال فایل', 'accept':
        ".pdf, .docx, .jpg, .png", 'draggable':"true"})


    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            # 'which_price_plan',
            'message',
            'file',
        ]