# coutureApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/', views.creerEtAfficher_client, name='client'),  # Utilisation de la vue pour création/affichage
    path('commande/', views.commande, name='commande'),
    path('tenue/', views.tenue, name='tenue'),
    path('image/', views.image, name='image'),
    path('facture/', views.facture, name='facture'),
    path('editefacture/', views.editefacture, name='editefacture'),
    path('clientlist/', views.clientlist, name='clientlist'),
    path('commandlist/', views.commandlist, name='commandlist'),
]




