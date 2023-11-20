from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='admission'),
    path('register/', register_user, name="register_user"),
    path('accuiel/', pages_accuiel_view, name='accuiel'),
    path('profil/', profil_view, name='profil'),
    path('deconnexion/',deconnexion_view,name='deconnexion'),
    path('modification_profil/',modification_profil_view,name='modification_profil'),

]
