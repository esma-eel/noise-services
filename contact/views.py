from django.shortcuts import render, redirect
from .models import Contact, ContactIntro
from .forms import ContactForm
from django.contrib import messages
from landing.models import Navigation



# Create your views here.
def contact_view(request):
    navigation_links = Navigation.objects.filter(for_footer=False).all()
    contact_intro = ContactIntro.objects.filter(active=True).first()
    form = ContactForm(request.POST or None, request.FILES or None)
    success_message = 'پیام شما با موفقیت ارسال شد، پس از بررسی با شما ارتباط برقرار خواهیم کرد'
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, success_message)
            return redirect('contact')

    contextvar = {
        'contact_form': form,
        'navigation_links': navigation_links,
        'contact_intro':contact_intro,
    }

    return render(request, 'contact/contact.html', contextvar)




