from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Tenue,Commande,Client


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
        

