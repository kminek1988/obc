from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .decorators import unauthenticated_user
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.views.generic import TemplateView, DetailView, ListView
from accounts.forms import RejestracjaForm, ProfileForm
from listy.models import Category
from accounts.models import Profil
# do rejestracji z mailem
from verify_email.email_handler import send_verification_email
#do rejestracji użytkownika
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#delete usse
from django.contrib import messages
from .forms import UserDeleteForm
UserModel = get_user_model()
#from .forms import SignUpForm
#from .tokens import account_activation_token
# REJESTRACJA URZYTKOWNIKA!!!!!

def rejestracja(request):
    if request.method == 'GET':
        return render(request, 'rejestracja.html')
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktywuj konto w obcbaden'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'accounts/confirm.html')
            # return HttpResponse('Przejdź do swojej poczty emial i dokończ rejestrację')
    else:
        form = RejestracjaForm()
    return render(request, 'rejestracja.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


#def rejestracja(request):
 #   form = RejestracjaForm(request.POST)

  #  if request.method == 'POST':
   #     if form.is_valid():
    #        inactive_user = send_verification_email(request, form)
     #       inactive_user.cleaned_data['email']

      #  return redirect('profil')
   # else:
    #    form = RejestracjaForm(request.POST)
     #   context = {'form':form }
      #  return render(request, 'rejestracja.html', context)

# PROFIL EDIT

@login_required
def Edycja(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES, instance=request.user.profil)  # request.FILES is show the selected image or file

        if form.is_valid():
            form.save()
            return redirect('profil')
    else:

        form = ProfileForm(instance=request.user.profil)
    return render(request, 'edit_profil.html', {'form':form})



# def  Edycja(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return render(request, 'profil.html')
#     else:
#         form = ProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'edit_profil.html', args)
#







# PROFIL
@login_required
def profil(request, pk=None):
    opis = request.user.profil
    context = {'opis': opis,

               }
    return render(request, 'profil.html', context)


#delete accounts


# class deleteuser(DetailView):
#     model = Profil
#     def user_passes_test(self, request):
#         if request.user.is_authenticated:
#             self.object = self.get_object()
#             return self.object.user == request.user
#         return False
