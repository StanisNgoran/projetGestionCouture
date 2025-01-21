from django.contrib import admin
from .models import Client,Commande,Tenue,ImageModele

admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Tenue)
admin.site.register(ImageModele)

# Modifier le titre de la page d'administration
admin.site.site_header = "Clothe Administration"
admin.site.site_title = "Clothe Admin"
admin.site.index_title = "Bienvenue sur le Tableau de Bord"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'contact')  # Colonnes affichées dans la liste
    list_filter = ('nom',)  # Filtrer par nom
    search_fields = ('nom', 'prenom')  # Ajouter une barre de recherche
    ordering = ('ajout',)  # Trier par nom


    fieldsets = (
        ("Informations Personnelles", {'fields': ('nom', 'prenom')}),
        ("Contact", {'fields': ('contact',)}),
    )



class CommandeAdmin(admin.ModelAdmin):
    list_display = ('debutcom', 'fincom', 'montancom','statut','dateretrait','idclient','creation')  # Colonnes affichées dans la liste
    list_filter = ('creation',)  # Filtrer par nom
    search_fields = ('nom', 'prenom')  # Ajouter une barre de recherche
    ordering = ('creation',)  # Trier par nom


    # fieldsets = (
    #     ("Informations Personnelles", {'fields': ('debutcom', 'fincom')}),
    #     ("Contact", {'fields': ('contact',)}),
    # )

