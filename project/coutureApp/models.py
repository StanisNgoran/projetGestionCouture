from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from datetime import datetime


class Profil(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('utilisateur', 'Utilisateur'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='utilisateur')

    def __str__(self):
        return f"{self.user.username} - {self.role}"   

def generate_client_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format : AnnéeMoisJourHeureMinuteSeconde
    return f"{timestamp}"


class Client(models.Model):
    idclient = models.CharField(primary_key=True, max_length=20,default=generate_client_id,unique=True)
    nom_prenom = models.CharField(max_length=100, null=True, blank=True)
    contact= models.CharField(max_length=100, null=True, blank=True)
    sexe = models.CharField(max_length=10, null=True, blank=True)
    ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} "
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    


def generate_commande_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format : AnnéeMoisJourHeureMinuteSeconde
    return f"{timestamp}"

class Commande(models.Model):
    idcom = models.CharField(primary_key=True,max_length=20,default=generate_commande_id,unique=True)
    idclient = models.ForeignKey(Client, on_delete=models.CASCADE)
    debutcom = models.DateField(auto_now_add=True)
    fincom = models.DateField()
    montantcom=models.IntegerField(default=0)
    statut=models.CharField(default="En Cours", max_length=51)
    methodePayement= models.CharField(default="Espece",max_length=20)
    dateretrait=models.DateTimeField(default=timezone.now)
    creation=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Commande {self.idcom}"
    
    def nbrCommande(self):
        for i in Commande:
            total=self.idcom.count()
        return total


# ____________________________________________________________________________________
#  PERMET DE CALCULER LE MONTANT TOTAL DE CHAQUE TENUE EN FONCTION DE SA QUANTITE ET DE SON PRIX UNITAIRE
# ____________________________________________________________________________________
   
    def calculer_montant_total(self):
        # Récupère toutes les tenues associées à cette commande
        tenues = self.tenue_set.all()
        total = sum(tenue.montant for tenue in tenues)
        self.montantcom = total
        self.save()  # Sauvegarde du nouveau montant
        return total
    
    
# ____________________________________________________________________________________
#  PERMET DE CALCULER LE NOMBRE DE TENUES DISTINCTES DANS UNE COMMANDE DONNEE
# ____________________________________________________________________________________

    def calculer_NombreTenue(self):
        tenues=self.tenue_set.all()
        nbr=sum(tenue.qte for tenue in tenues)
        return nbr
        # return self.tenue_set.count()
        
    


def generate_tenue_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format : AnnéeMoisJourHeureMinuteSeconde
    return f"{timestamp}"


class Tenue(models.Model):
    idtenu = models.CharField(primary_key=True, max_length=20,default=generate_tenue_id,unique=True)
    idcom = models.ForeignKey(Commande, on_delete=models.CASCADE ,default=1)
    prix = models.IntegerField()
    avance = models.IntegerField()
    reste = models.IntegerField()
    montant=models.IntegerField(default=prix)
    qte=models.IntegerField(default=1)
    modele = models.TextField()
    ajout = models.DateTimeField(auto_now_add=True)
    etat_tenue=models.CharField(max_length=100, blank=True)
   
    def __str__(self):
        return self.description
    



# ____________________________________________________________________________________
#  PERMET DE CALCULER LE MONTANT TOTAL DE CHAQUE TENUE EN FONCTION DE SA QUANTITE ET DE SON PRIX UNITAIRE
# ____________________________________________________________________________________

    def calculer_montant(self):
            # Calcule le montant en fonction de la quantité et du prix
            self.montant = self.qte * self.prix
            self.reste = self.montant - self.avance
            self.save()  # Sauvegarde les valeurs calculées
            return self.montant
    




def generate_facture_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format : AnnéeMoisJourHeureMinuteSeconde
    return f"{timestamp}"

class Facture(models.Model):
    idfacture = models.CharField(primary_key=True,max_length=20,default=generate_facture_id,unique=True)
    idcom = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Facture {self.idfacture}"
    

    def get_details(self):
        tenues = self.idcom.tenue_set.all()  # Toutes les tenues de la commande
        return {
            "client": self.idclient,
            "commande": self.idcom,
            "tenues": tenues,
            "date_facture": self.date_facture,
        }



def generate_image_id():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Format : AnnéeMoisJourHeureMinuteSeconde
    return f"{timestamp}"

class ImageModele(models.Model):
    idmg = models.CharField(primary_key=True,max_length=20,default=generate_image_id,unique=True)
    idtenu = models.ForeignKey(Tenue, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='tenue_images/', null=True, blank=True)
    ajout = models.DateTimeField(auto_now_add=True)
