# coutureApp/views.py
from django.shortcuts import render, redirect
from.models import Client
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def client(request):
    return render (request,'client.html')

def commande(request):
    return render (request,'commande.html')
# Create your views here.

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
        
        # Créer un nouvel objet Client et l'enregistrer dans la base de données
        client = Client(nom=nom, prenom=prenom, contact=contact)
        client.save()
        messages.success(request, 'Client Enregistré avec Succès!')
        # Rediriger vers la même page pour afficher le client nouvellement ajouté
        return redirect('commande')  # Rediriger vers la même vue pour éviter les re-soumissions

    # Récupère tous les clients pour les afficher dans le tableau
    clients = Client.objects.all().order_by('-ajout')
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})  # Utilisez 'clients' ici

