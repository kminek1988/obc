from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contact.models import Contact
from accounts.models import Profil
from contact.forms import ContactForm

# Create your views here.

def add_or_change_contact(request, username=None):

    form = ContactForm(request.POST)
    user = request.user

    if request.method == 'POST':
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.owner = user
            new_coment.save()

            #form.save()
        return redirect('profil')
    else:
        form = ContactForm(request.POST)
        context = {'form':form }
        return render(request, 'ContactForm.html', context)