# coutureApp/urls.py
from django.urls import path
from . import views
from .views import register, login_view, logout_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
 
    path('home/', views.home, name='home'),

    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('client/', views.Ajouter_client, name='client'),  # Utilisation de la vue pour création/affichage
    path('commande/<str:idclient>', views.SaveCommande, name='commande'),

    path('HistoriqueTenue/', views.Historique_Tenue, name='HistoriqueTenue'),
    path('ActionRetrait/<str:idcom>', views.Action_Retrait, name='actionRetrait'),
    path('ListeRetraitCommande/', views.Liste_de_retrait, name='retraitCommande'),
    path('HistoriqueCommande/', views.Historique_de_commande, name='HistoriqueCommande'),
    path('InfosCommande/<str:idcom>', views.infosCommande, name='infosCommande'),
    path('tenue/<str:idcom>', views.tenue, name='tenue'),
    path('InfosTenue/<str:idtenu>', views.infostenue, name='infosTenue'),
    path('image/<str:idtenu>', views.image, name='image'),

    path('modifierimage/<str:idmg>/', views.modifier_image, name='modifierImage'),
    path('supprimerimage/picture/<str:idmg>/', views.supprimer_image, name='suppImage'),
    path('facture/', views.facture, name='facture'),
    path('createfacture/', views.createfacture, name='createfacture'),
    path('editefacture/Enregistrement/<str:idcom>/', views.editefacture, name='editefacture'),
    path('Aff_Facture/Vue/<str:idfacture>/', views.Aff_Facture, name='Aff_Facture'),
    path('supprimerfacture/<str:idfacture>/', views.supprimer_facture, name='supprimer_facture'),
    path('modifierfacture/<str:idfacture>/', views.modifier_facture, name='modifierFacture'),

    path('commande/ajouter/<str:idclient>/', views.SaveCommande, name='commande'),
    path('clientlist/', views.clientlist, name='clientlist'),
    path('commandlist/', views.commandlist, name='commandlist'),
    path('album/', views.album, name='album'),
    path('listeTenue/', views.listeTenue, name='listeTenue'),
    path('statistique/', views.statistique, name='statistique'),

    path('client/supprimer/<str:idclient>/', views.supprimer_client, name='supprimer_client'),
    path('client/modifier/<str:idclient>/', views.modifier_client, name='modifier_client'),

    path('commande/modifier/<str:idcom>/',views.modifier_commande,name="modifier_commande"),
    path('commande/supprimer/<str:idcom>/',views.supprimer_commande,name="supprimer_commande"),
    
    path('tenue/modifier/<str:idtenu>/',views.modifier_tenue,name="modifier_tenue"),
    path('tenue/supprimer/<str:idtenu>/',views.supprimer_tenue,name="supprimer_tenue"),

    


    
]




