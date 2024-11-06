# coutureApp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from.models import Client
from.models import Commande
from django.contrib import messages
from datetime import datetime,timezone


def home(request):

    # Permet d'afficher toutes les commandes dans un tableau
    commandes = Commande.objects.all()

    # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all()


    today = datetime.now(timezone.utc)  
    for commande in commandes:
        # Calcul du nombre de jours restants et ajout en tant qu'attribut
        commande.jour_restant = (commande.fincom - today).days if commande.fincom else None

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'home.html', {'commandes': commandes})



def client(request):
    return render (request,'client.html')


def tenue(request):
    return render (request,'tenue.html')

def image(request):
    return render(request,'image.html')

def facture(request):
    return render(request,'facture.html')

def editefacture(request):
    return render(request,'editefacture.html')

def clientlist(request):
    return render(request,'clientlist.html')


def commandlist(request):
    return render(request,'commandlist.html')


   
def creerEtAfficher_client(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        contact = request.POST.get('contact')
        
        if nom=="":
            messages.error(request, "Veuillez Entrer le nom du client.")
            return redirect('client')
        elif prenom=="":
            messages.error(request, "Veuillez Entrer le prenom du client.")
            return redirect('client')
        
        elif contact=="":
            messages.error(request, "Veuillez saisir le contact.")
            return redirect('client')

        elif contact and (len(contact)!=10 or not contact.isdigit()):
            messages.error(request, "Le contact doit etre 10 chiffres.")
            return redirect('client')
        else:



            # Créer un nouvel objet Client et l'enregistrer dans la base de données
            client = Client(nom=nom, prenom=prenom, contact=contact)
            client.save()
            messages.success(request, 'Client Enregistré avec Succès!')
            # Rediriger vers la même page pour afficher le client nouvellement ajouté
            return redirect('commande')  # Rediriger vers la même vue pour éviter les re-soumissions

    # Récupère tous les clients pour les afficher dans le tableau

    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})  # Utilisez 'clients' ici


def SaveCommande(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idclient = request.POST.get("idclient")
        debutcom = request.POST.get("debutcom")
        fincom = request.POST.get("fincom")

         # Vérifie que `idclient` est valide et récupère l'instance `Client` clé étrangère
        client_instance = get_object_or_404(Client, pk=idclient)
        
        # Enregistrement de la commande si son client existe

        if not idclient:

            messages.error(request, "Veuillez sélectionner un client valide.")
            return redirect('commande')
        
        elif debutcom=="":
            messages.error(request, "Veuillez selectionner la date du debut.")
            return redirect('commande')
        
        elif fincom=="":
            messages.error(request, "Veuillez selectionner la date de fin.")
            return redirect('commande')
        
        elif fincom<debutcom:
            messages.error(request, "La date de fin doit être après la date de début.")
            return redirect('commande')


           
        else:
            
            commande = Commande(idclient=client_instance, debutcom=debutcom, fincom=fincom)
            commande.save()
            messages.success(request, 'Commande Enregistrée avec Succès!')
            return redirect('tenue')

    # Permet d'afficher toutes les commandes dans un tableau
    commandes = Commande.objects.all()

    # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all()


    today = datetime.now(timezone.utc)  
    for commande in commandes:
        # Calcul du nombre de jours restants et ajout en tant qu'attribut
        commande.jour_restant = (commande.fincom - today).days if commande.fincom else None

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'commande.html', {'commandes': commandes, 'clients': clients})


       
    
    