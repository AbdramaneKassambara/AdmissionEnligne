from django.conf import settings
from email.message import EmailMessage

import smtplib
from django.shortcuts import render, redirect
from django.contrib import messages

# from .Class import Comptes
from .models import Utilisateurs
def login_view(request):
    response = ''
    if request.method == 'POST':
        code_user = request.POST.get('code_user')
        password = request.POST.get('password')
        user, success = Utilisateurs.login_user(code_user=code_user, password=password)
        if success:
            request.session['user_id'] = user.get('id')
           # response.set_cookie('code_user', code_user)
            response= redirect('accuiel')
            return response
        else:
            messages.warning(request, "Votre nom d'utilisateur ou votre mot de passe est incorrecte !!!")
            return render(request, 'Utilisateurs/login.html')
    return render(request, 'Utilisateur/login.html')

def register_user(request):
    if request.method == "POST":
        code_user = request.POST.get('code_user')
        password = request.POST.get('password')
        email = request.POST.get('email')
        new_user = Utilisateurs(code_user=code_user, password=password, email=email, actifs=True)
        new_user.save()
        return redirect("admission")
    return render(request, 'Utilisateur/registre.html')


def pages_accuiel_view(request):
    id_user = request.session['user_id']
    info_user,success = Utilisateurs.get_user_id(id_user)
    if success:
        context = {
            'info_user' : info_user,
        }
        return render(request,'Utilisateur/accueil.html',context=context)
    return render(request, 'Utilisateur/accueil.html')


def profil_view(request):
    id_user = request.session['user_id']
    info_user,success = Utilisateurs.get_user_id(id_user)
    if success:
        context = {
            'info_user' : info_user,
        }
        return render(request,'Utilisateurs/accueil.html',context=context)
    return render(request, 'Utilisateur/profil.html')
def deconnexion_view(request):
    del request.session['user_id']
    return redirect('admission')

def modification_profil_view(request):
    return render(request, 'Utilisateur/modification_profil.html');