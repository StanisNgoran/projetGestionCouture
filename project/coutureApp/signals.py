from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tenue

@receiver(post_save, sender=Tenue)
def update_commande_montant(sender, instance, **kwargs):
    # Appelle la méthode de calcul pour mettre à jour montantcom
    instance.idcom.calculer_montant_total()
