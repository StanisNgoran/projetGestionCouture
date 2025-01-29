from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Tenue,Commande,Client
from django.contrib.auth.models import User
from .models import Profil

# Signal pour mettre à jour le montant total de la commande après modification d'une tenue
@receiver(post_save, sender=Tenue)
def mettre_a_jour_montant_commande(sender, instance, **kwargs):
    commande = instance.idcom
    if commande:
        commande.calculer_montant_total()





# Signal pour mettre à jour le nbr de  tenues distinctes dans une commande après modification d'une tenue
@receiver(post_save,sender=Tenue)
def mettre_a_jour_nbr_tenue_dans_commande(sender,instance,**kwargs):
    commande=instance.idcom
    if commande:
        commande.calculer_NombreTenue()
        



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance,role="utilisateur")



# @receiver(post_save, sender=Profil)
# def sauvegarder_profil(sender, instance, **kwargs):
#     instance.save()


# Suppression du profil et de l'utilisateur
# 
@receiver(post_delete,sender=Profil)
def suppressionUser(sender,instance,**kwargs):
    utilisateur=instance.user
    if utilisateur:
        utilisateur.delete()