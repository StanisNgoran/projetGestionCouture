# coutureApp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from.models import Client
from.models import Commande
from.models import Tenue
from.models import ImageModele
from django.contrib import messages
from datetime import datetime,timezone

def supprimer_client(request,idclient):
    # Récupère le client ou renvoie une erreur 404 si non trouvé
    client = get_object_or_404(Client, pk=idclient)

    # Supprime le client
    client.delete()

    # Affiche un message de confirmation (facultatif)
    messages.success(request, "Client supprimé avec succès!")
    

    return redirect('clientlist')


def modifier_client(request,idclient):
    # Récupère le client ou renvoie une erreur 404 si non trouvé
    client = get_object_or_404(Client, idclient=idclient)
    if request.method == 'POST':
            # Récupérer les nouvelles valeurs des champs
            client.nom = request.POST.get('nom', client.nom)  # Garde la valeur existante si vide
            client.prenom = request.POST.get('prenom', client.prenom)
            client.contact = request.POST.get('contact', client.contact)

            # Sauvegarder les nouvelles valeurs dans la base de données
            client.save()
            # Ajouter un message de succès
            messages.success(request, 'Client modifié avec succès.')
            # clients=Client.objects.all()
            return redirect('clientlist')  # Rediriger vers la liste des clients
            
    return render(request, 'modifierClient.html', {'client': client})







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



def tenue(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idcom = request.POST.get("idcom")
        prix = request.POST.get("prix")
        avance = request.POST.get("avance")
        modele = request.POST.get("modeltenue")
        description = request.POST.get("description")


         # Vérifie que `idclient` est valide et récupère l'instance `Client` clé étrangère
        commande_instance = get_object_or_404(Commande, pk=idcom)
        
        # Enregistrement de la commande si son client existe

        if not idcom:

            messages.error(request, "Veuillez sélectionner une commande valide.")
            return redirect('tenue')
        
        elif prix=="" or not prix.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir un prix valide et superieur à 0.")
            return redirect('tenue')
        
        elif avance=="" or not avance.isdigit() or avance>prix:
            messages.error(request, "Veuillez saisir une avance valide!.")
            return redirect('tenue')
        
        elif modele=="":
            messages.error(request, "Veuillez selectionner un modele")
            return redirect('tenue')

           
        else:
            prix_converti=int(prix)
            avance_converti=int(avance)
            reste=prix_converti-avance_converti
            tenue = Tenue(idcom=commande_instance, prix=prix_converti, avance=avance_converti,reste=reste,modele=modele,description=description)
            tenue.save()
            messages.success(request, 'Tenue Ajoutée avec Succès!')
            return redirect('image')

    # Permet d'afficher toutes les commandes dans un tableau
    tenues = Tenue.objects.all()

    # permet de remplir le comboBox des ID du client 
    commands = Commande.objects.all()
    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'tenue.html', {'tenues': tenues, 'commands': commands})

    

def image(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idtenu = request.POST.get("idtenu")
        # photos = request.POST.get("photos")
        photos = request.FILES.get("photos")
        libelle = request.POST.get("libelle")


         # Vérifie que `id` est valide et récupère l'instance `Client` clé étrangère
        tenue_instance = get_object_or_404(Tenue, pk=idtenu)
        
        

        if not idtenu:

            messages.error(request, "Veuillez sélectionner une tenue valide.")
            return redirect('image')
        
        elif not photos:
            messages.error(request, "Veuillez joindre une image de modele.")
            return redirect('image')
        
        elif libelle=="":
            messages.error(request, "Veuillez ajouter un libellé ou un commentaire.")
            return redirect('image')
           
        else:
            imagemodele = ImageModele(idtenu=tenue_instance, photos=photos, libelle=libelle)
            imagemodele.save()
            messages.success(request, 'Image Ajoutée avec Succès!')
            return redirect('image')

    # Permet d'afficher les ID des tenues dans le comboBox
    tenues = Tenue.objects.all()

    # permet de remplir le comboBox 
    imagemodeles = ImageModele.objects.all()
    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'image.html', {'imagemodeles': imagemodeles, 'tenues': tenues})




def facture(request):
    return render(request,'facture.html')

def editefacture(request):
    return render(request,'editefacture.html')

def clientlist(request):
    clients=Client.objects.all()
    return render(request,'clientlist.html',{'clients':clients})


def commandlist(request):
    return render(request,'commandlist.html')

def album(request):
    return render(request,'album.html')

def listeTenue(request):
    return render(request,'listeTenue.html')

def statistique(request):
    return render(request,'statistique.html')
   

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


       
    
    