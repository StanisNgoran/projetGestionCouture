# coutureApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/', views.creerEtAfficher_client, name='client'),  # Utilisation de la vue pour création/affichage
    path('commande/', views.SaveCommande, name='commande'),
    path('tenue/', views.tenue, name='tenue'),
    path('image/', views.image, name='image'),
    path('facture/', views.facture, name='facture'),
    path('editefacture/Enregistrement/<int:idcom>/', views.editefacture, name='editefacture'),
    # path('Aff_Facture/Vue/<int:idcom>/', views.Aff_Facture, name='Aff_Facture'),
    path('Aff_Facture/Vue/<int:idfacture>/', views.Aff_Facture, name='Aff_Facture'),

    path('clientlist/', views.clientlist, name='clientlist'),
    path('commandlist/', views.commandlist, name='commandlist'),
    path('album/', views.album, name='album'),
    path('listeTenue/', views.listeTenue, name='listeTenue'),
    path('statistique/', views.statistique, name='statistique'),

    path('client/supprimer/<int:idclient>/', views.supprimer_client, name='supprimer_client'),
    path('client/modifier/<int:idclient>/', views.modifier_client, name='modifier_client'),

    path('commande/modifier/<int:idcom>/',views.modifier_commande,name="modifier_commande"),
    path('commande/supprimer/<int:idcom>/',views.supprimer_commande,name="supprimer_commande"),
    
    path('tenue/modifier/<int:idtenu>/',views.modifier_tenue,name="modifier_tenue"),
    path('tenue/supprimer/<int:idtenu>/',views.supprimer_tenue,name="supprimer_tenue"),

    


    
]




