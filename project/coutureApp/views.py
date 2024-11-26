# coutureApp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from.models import Client
from.models import Commande
from.models import Tenue
from.models import ImageModele
from django.contrib import messages
from datetime import datetime,timezone





# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS PRESENTES DANS HOME(MENUE PRINCIPAL) 
# ____________________________________________________________________________________

def home(request):

    # Permet d'afficher toutes les commandes dans un tableau
    commandes = Commande.objects.all()

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'home.html', {'commandes': commandes})







# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES CLIENTS 
# ____________________________________________________________________________________

# Creation du client 
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



# Affiche la liste des clients à modifier 
def clientlist(request):
    clients=Client.objects.all()
    return render(request,'clientlist.html',{'clients':clients})

# Permet de modifier un client 
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

            return redirect('clientlist')  # Rediriger vers la liste des clients
            
    return render(request, 'modifierClient.html', {'client': client})


# permet de supprimer un client 
def supprimer_client(request,idclient):
    # Récupère le client ou renvoie une erreur 404 si non trouvé
    client = get_object_or_404(Client, pk=idclient)

    # Supprime le client
    client.delete()

    # Affiche un message de confirmation (facultatif)
    messages.success(request, "Client supprimé avec succès!")
    return redirect('clientlist')








# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES COMMANDES 
# ____________________________________________________________________________________


# Permet d'afficher la liste des commandes à modifier
def commandlist(request):
    commandes=Commande.objects.all()
    for commande in commandes:
        commande.nombre_tenue=commande.calculer_NombreTenue()
    return render(request,'commandlist.html',{'commandes':commandes})


# Enregistrement de la commande d'un client donné 
def SaveCommande(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idclient = request.POST.get("idclient")
        debutcom = request.POST.get("debutcom")
        fincom = request.POST.get("fincom")
        
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
            # Vérifie que `idclient` est valide et récupère l'instance `Client` clé étrangère
            client_instance = get_object_or_404(Client, pk=idclient)
            commande = Commande(idclient=client_instance, debutcom=debutcom, fincom=fincom)
            commande.save()
            messages.success(request, 'Commande Enregistrée avec Succès!')
            return redirect('tenue')

    # Permet d'afficher toutes les commandes dans un tableau
    commandes = Commande.objects.all()
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

    # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all()

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'commande.html', {'commandes': commandes, 'clients': clients})




# Permet de modifier une commande
def modifier_commande(request,idcom):
    commande= get_object_or_404(Commande,idcom=idcom)
    if request.method=='POST':
        commande.debutcom=request.POST.get('debutcom',commande.debutcom)
        commande.fincom=request.POST.get('fincom',commande.fincom)
        commande.statut=request.POST.get('statut',commande.statut)
        
        if commande.debutcom=="":
            messages.error(request, "Veuillez selectionner la date du debut.")
            return redirect('modifier_commande',idcom=idcom)
        
        elif commande.fincom=="":
            messages.error(request, "Veuillez selectionner la date de fin.")
            return redirect('modifier_commande',idcom=idcom)
        
        elif commande.fincom<commande.debutcom:
            messages.error(request, "La date de fin doit être après la date de début.")
            return redirect('modifier_commande',idcom=idcom)
        else:

            commande.save()
            messages.success(request,'Commande modifiée avec Succès')
            return redirect('commandlist')
    return render(request,'modifierComand.html',{'commande':commande})


# Permet de supprimer une commande
def supprimer_commande(request,idcom):
    commande=get_object_or_404(Commande,pk=idcom)
    commande.delete()
    messages.success(request,'Commande supprimée avec succès')

    return redirect('commandlist')







# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES TENUES 
# ____________________________________________________________________________________


# Permet d'afficher la liste des tenues
def listeTenue(request):
    tenues=Tenue.objects.all()
    return render(request,'listeTenue.html',{'tenues':tenues})


# Permet de modifier une tenue 

def modifier_tenue(request,idtenu):
    tenue=get_object_or_404(Tenue,idtenu=idtenu)
    if request.method=="POST":
        tenue.prix=request.POST.get("prix",tenue.prix)
        tenue.avance=request.POST.get("avance",tenue.avance)
        tenue.modele=request.POST.get("modeltenue",tenue.modele)
        tenue.description=request.POST.get("description",tenue.description)
        tenue.qte=request.POST.get("qte",tenue.qte)

        qte=int(tenue.qte)
        prix_cal=int(tenue.prix)
        avance_cal=int(tenue.avance)
        tenue.montant=qte*prix_cal
        tenue.reste=tenue.montant-avance_cal
        

        if tenue.reste<=0:
            tenue.etat_tenue="Soldé"
            tenue.save()
            messages.success(request,"Tenue modifiée avec succès")
            return redirect('listeTenue')
        else:
            tenue.etat_tenue="Non Soldé"
            tenue.save()
            messages.success(request,"Tenue modifiée avec succès")
            return redirect('listeTenue')
    return render(request,"modifierTenue.html",{'tenue':tenue})

# Permet de supprimer une tenue dans une commande 
def supprimer_tenue(request,idtenu):
    tenue=get_object_or_404(Tenue,pk=idtenu)
    tenue.delete()
    messages.success(request,"Tenue supprimée avec succès")
    return redirect('listeTenue')



# Permet d'enregistrer une tenue dans la commande
def tenue(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idcom = request.POST.get("idcom")
        prix = request.POST.get("prix")
        qte=request.POST.get("qte")
        avance = request.POST.get("avance")
        modele = request.POST.get("modeltenue")
        description = request.POST.get("description")
        
        # Enregistrement de la commande si son client existe

        if not idcom:

            messages.error(request, "Veuillez sélectionner une commande valide.")
            return redirect('tenue')
        
        elif prix=="" or not prix.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir un prix valide et superieur à 0.")
            return redirect('tenue')
        
        elif prix=="" or not prix.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir un prix valide et superieur à 0.")
            return redirect('tenue')
        
        elif qte=="" or not qte.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir une quantité valide et superieur à 0.")
            return redirect('tenue')
        
        elif avance=="" or not avance.isdigit() or avance>prix:
            messages.error(request, "Veuillez saisir une avance valide!.")
            return redirect('tenue')
        
        elif modele=="":
            messages.error(request, "Veuillez selectionner un modele")
            return redirect('tenue')


           
        else:
            
         # Vérifie que `idclient` est valide et récupère l'instance `Client` clé étrangère
            commande_instance = get_object_or_404(Commande, pk=idcom)
            prix_converti=int(prix)
            avance_converti=int(avance)
            qte=int(qte)
            montant=qte*prix_converti
            reste=montant-avance_converti
           
            


            if montant==avance_converti:
                tenue = Tenue(idcom=commande_instance, prix=prix_converti, qte=qte,montant=montant, avance=avance_converti,reste=reste,modele=modele,description=description,etat_tenue="Soldé")
                tenue.save()
                messages.success(request, 'Tenue Ajoutée avec Succès!')
                return redirect('image')
            elif reste>0:
                tenue = Tenue(idcom=commande_instance, prix=prix_converti,qte=qte,montant=montant, avance=avance_converti,reste=reste,modele=modele,description=description,etat_tenue="Non Soldé")
                tenue.save()
                messages.success(request, 'Tenue Ajoutée avec Succès!')
                return redirect('image')

    # Permet d'afficher toutes les commandes dans un tableau
    tenues = Tenue.objects.all()

    # permet de remplir le comboBox des ID du client 
    commands = Commande.objects.all()
    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'tenue.html', {'tenues': tenues, 'commands': commands})

    




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES IMAGES DES TENUES 
# __________________________________________________________________________________________


# Permet d'ajouter une image  à la tenue dans la commande
def image(request):
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        idtenu = request.POST.get("idtenu")
        # photos = request.POST.get("photos")
        photos = request.FILES.get("photos")
        libelle = request.POST.get("libelle")
        
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
            # Vérifie que `id` est valide et récupère l'instance `Client` clé étrangère
            tenue_instance = get_object_or_404(Tenue, pk=idtenu)
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





# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES FACTURES
# __________________________________________________________________________________________


def facture(request):
    commandes = Commande.objects.all()
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

    # # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all()

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'facture.html', {'commandes': commandes, 'clients': clients})


def editefacture(request):
    return render(request,'editefacture.html')








# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES ALBUMS 
# __________________________________________________________________________________________

def album(request):
    return render(request,'album.html')







# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES STATISTIQUES
# __________________________________________________________________________________________

def statistique(request):
    return render(request,'statistique.html')
   


       
    
    