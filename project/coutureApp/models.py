from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Commande(models.Model):
    idcom = models.AutoField(primary_key=True)
    idclient = models.ForeignKey(Client, on_delete=models.CASCADE)
    debutcom = models.DateField()
    fincom = models.DateField()
    montantcom=models.IntegerField(default=0)
    statut=models.CharField(default="En Attente", max_length=50)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande {self.idcom}"

    # def calculer_montant_total(self):
    #     # Récupère toutes les tenues associées à cette commande
    #     tenues = self.tenue_set.all()
    #     total = sum(tenue.qte * tenue.prix for tenue in tenues)
    #     self.montantcom = total
    #     self.save()  # Sauvegarde du nouveau montant
    #     return total


class Tenue(models.Model):
    idtenu = models.AutoField(primary_key=True)
    prix = models.IntegerField()
    avance = models.IntegerField()
    reste = models.IntegerField()
    montant=models.IntegerField(default=0)
    qte=models.IntegerField(default=0)
    modele = models.TextField()
    description = models.CharField(max_length=300)
    idcom = models.ForeignKey(Commande, on_delete=models.CASCADE ,default=1)
    ajout = models.DateTimeField(auto_now_add=True)
    etat_tenue=models.CharField(max_length=100, blank=True)
    modifierle=models.DateField(default= timezone.now)

    

    def __str__(self):
        return self.description
    

#     def calculer_montant(self):
#             # Calcule le montant en fonction de la quantité et du prix
#             self.montant = self.qte * self.prix
#             self.reste = self.montant - self.avance
#             self.save()  # Sauvegarde les valeurs calculées
#             return self.montant
    

# # Signal pour mettre à jour le montant total de la commande après modification d'une tenue
# @receiver(post_save, sender=Tenue)
# def mettre_a_jour_montant_commande(sender, instance, **kwargs):
#     commande = instance.idcom
#     if commande:
#         commande.calculer_montant_total()
        

class Facture(models.Model):
    idfacture = models.AutoField(primary_key=True)
    idclient = models.ForeignKey(Client, on_delete=models.CASCADE)
    idcom = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Facture {self.idfacture}"



class ImageModele(models.Model):
    idmg = models.AutoField(primary_key=True)
    idtenu = models.ForeignKey(Tenue, on_delete=models.CASCADE)
    #photos = models.BinaryField()  # Store image as binary
    photos = models.ImageField(upload_to='tenue_images/', null=True, blank=True)
    libelle = models.CharField(max_length=100)
    ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libelle


# class TenueCommande(models.Model):
#     idcom = models.ForeignKey(Commande, on_delete=models.CASCADE)
#     idtenu = models.ForeignKey(Tenue, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('idcom', 'idtenu')  # Prevent duplicate combinations

#     def __str__(self):
#         return f"Commande {self.idcom.idcom} - Tenue {self.idtenu.idtenu}"


