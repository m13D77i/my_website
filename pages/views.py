from django.shortcuts import render

from .forms import ContactForm

def home_page_view(request):
    return render(request, "pages/home.html")

def about_page_view(request):
    return render(request, "pages/about.html")

def contact_page_view(request):
    form = ContactForm()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "pages/contact.html", {'form': form})

