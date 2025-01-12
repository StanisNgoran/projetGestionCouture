# coutureApp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from.models import Client
from.models import Commande
from.models import Tenue
from.models import ImageModele,Facture
from django.contrib import messages
from datetime import datetime,timezone
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncWeek



# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS PRESENTES DANS HOME(MENUE PRINCIPAL) 
# ____________________________________________________________________________________

def home(request):

    # Permet d'afficher toutes les commandes dans un tableau
    commandes = Commande.objects.all().order_by('-creation')

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'home.html', {'commandes': commandes})




# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES CLIENTS 
# ____________________________________________________________________________________
# Creation du client 
def Ajouter_client(request):
    if request.method == 'POST':
        nom = request.POST['nom'].upper()
        prenom = request.POST['prenom'].upper()
        contact = request.POST['contact']
        
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
            return redirect('clientlist')  
    return render(request, 'client.html')  



# Affiche la liste des clients  
def clientlist(request):
    clients=Client.objects.all().order_by('-ajout')
    return render(request,'clientlist.html',{'clients':clients})




# Permet de modifier un client 
def modifier_client(request,idclient):
    # Récupère le client à modifier
    client_a_modifier = get_object_or_404(Client, idclient=idclient)
    if request.method == 'POST':
            # Récupérer les nouvelles valeurs des champs
            client_a_modifier.nom = request.POST.get('nom', client_a_modifier.nom) # Garde la valeur existante si vide
            client_a_modifier.prenom = request.POST.get('prenom', client_a_modifier.prenom)
            client_a_modifier.contact = request.POST.get('contact', client_a_modifier.contact)

            # Sauvegarder les nouvelles valeurs dans la base de données
            client_a_modifier.save()
            # Ajouter un message de succès
            messages.success(request, 'Client modifié avec succès.')

            return redirect('clientlist')  # Rediriger vers la liste des clients
    return render(request, 'modifierClient.html', {'client': client_a_modifier})



# permet de supprimer un client 
def supprimer_client(request,idclient):
    client_a_supprimer = get_object_or_404(Client, idclient=idclient)
    # Supprime le client
    client_a_supprimer.delete()

    # Affiche un message de confirmation (facultatif)
    messages.success(request, "Client supprimé avec succès!")
    return redirect('clientlist')








# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES COMMANDES 
# ____________________________________________________________________________________

# Permet d'afficher la liste des commandes à modifier
def commandlist(request):
    commandes=Commande.objects.all().order_by('-creation')
    for commande in commandes:
        commande.nombre_tenue=commande.calculer_NombreTenue()
    return render(request,'commandlist.html',{'commandes':commandes})



# Enregistrement de la commande d'un client donné 
def SaveCommande(request,idclient):
    client_commandeur = get_object_or_404(Client, idclient=idclient)
    if request.method == "POST":
        # Récupération des valeurs depuis le formulaire
        debutcom = request.POST["debutcom"]
        fincom = request.POST["fincom"]
        
        # Enregistrement de la commande si son client existe

        if debutcom=="":
            messages.error(request, "Veuillez selectionner la date du debut.")
            return redirect('commande',idclient=idclient)
        
        elif fincom=="":
            messages.error(request, "Veuillez selectionner la date de fin.")
            return redirect('commande',idclient=idclient)
        
        elif fincom<debutcom:
            messages.error(request, "La date de fin doit être après la date de début.")
            return redirect('commande',idclient=idclient)
    
        else:
            
            commande_lierauclient = Commande(idclient=client_commandeur, debutcom=debutcom, fincom=fincom)
            commande_lierauclient.save()
            messages.success(request, 'Commande Enregistrée avec Succès!')
            return redirect('tenue',commande_lierauclient.idcom)
    return render(request, 'commande.html', {'client': client_commandeur})




# Permet de modifier une commande
def modifier_commande(request,idcom):
    commande_a_modifier= get_object_or_404(Commande,idcom=idcom)
    if request.method=='POST':
        commande_a_modifier.debutcom=request.POST.get('debutcom',commande_a_modifier.debutcom)
        commande_a_modifier.fincom=request.POST.get('fincom',commande_a_modifier.fincom)
        commande_a_modifier.statut=request.POST.get('statut',commande_a_modifier.statut)
        
        if commande_a_modifier.debutcom=="":
            messages.error(request, "Veuillez selectionner la date du debut.")
            return redirect('modifier_commande',idcom=idcom)
        
        elif commande_a_modifier.fincom=="":
            messages.error(request, "Veuillez selectionner la date de fin.")
            return redirect('modifier_commande',idcom=idcom)
        
        elif commande_a_modifier.fincom<commande_a_modifier.debutcom:
            messages.error(request, "La date de fin doit être après la date de début.")
            return redirect('modifier_commande',idcom=idcom)
        else:

            commande_a_modifier.save()
            messages.success(request,'Commande modifiée avec Succès')
            return redirect('commandlist')
    return render(request,'modifierComand.html',{'commande':commande_a_modifier})



def infosCommande(request,idcom):
    commande=get_object_or_404(Commande,idcom=idcom)
    tenue_commandee=commande.tenue_set.all()
    details={
        "tenues":tenue_commandee,
        "total_commande":commande.montantcom


    }

    return render(request,"infosCommande.html",{'details':details,'commande':commande})

# Permet de supprimer une commande
def supprimer_commande(request,idcom):
    commande=get_object_or_404(Commande,idcom=idcom)
    commande.delete()
    messages.success(request,'Commande supprimée avec succès')
    return redirect('commandlist')







# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES TENUES 
# ____________________________________________________________________________________


# Permet d'afficher la liste des tenues
def listeTenue(request):
    tenues=Tenue.objects.all().order_by("-ajout")
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
def tenue(request,idcom):
    commande_instance=get_object_or_404(Commande,idcom=idcom)
    if request.method == "POST":
       
        prix = request.POST.get("prix")
        qte=request.POST.get("qte")
        avance = request.POST.get("avance")
        modele = request.POST.get("modeltenue")
        description = request.POST.get("description")
        
        # Enregistrement de la commande si son client existe
        prix_converti=int(prix)
        qte_cov=int(qte)
        avance_converti=int(avance)


        
        if prix=="" or not prix.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir un prix valide et superieur à 0.")
            return redirect('tenue',idcom=idcom)
        
        elif prix=="" or not prix.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir un prix valide et superieur à 0.")
            return redirect('tenue',idcom=idcom)
        
        elif qte=="" or not qte.isdigit() or prix<='0':
            messages.error(request, "Veuillez saisir une quantité valide et superieur à 0.")
            return redirect('tenue',idcom=idcom)
        

        elif avance=="" or not avance.isdigit():
            messages.error(request, "Veuillez saisir une avance valide!.")
            return redirect('tenue',idcom=idcom)
        

        elif modele=="":
            messages.error(request, "Veuillez selectionner un modele")
            return redirect('tenue',idcom=idcom)
        

        elif avance_converti>(qte_cov*prix_converti):
            messages.error(request, " Erreur L'avance depasse le montant total des tenues")
            return redirect('tenue',idcom=idcom)

           
        else:
            prix_converti=int(prix)
            avance_converti=int(avance)
            qte=int(qte)
            montant=qte*prix_converti
            reste=montant-avance_converti
 
            if montant==avance_converti:
                tenue_commandee = Tenue(idcom=commande_instance, prix=prix_converti, qte=qte,montant=montant, avance=avance_converti,reste=reste,modele=modele,description=description,etat_tenue="Soldé")
                tenue_commandee.save()
                messages.success(request, 'Tenue Ajoutée avec Succès!')
                return redirect('image')
            elif reste>0:
                tenue_commandee = Tenue(idcom=commande_instance, prix=prix_converti,qte=qte,montant=montant, avance=avance_converti,reste=reste,modele=modele,description=description,etat_tenue="Non Soldé")
                tenue_commandee.save()
                messages.success(request, 'Tenue Ajoutée avec Succès!')
                return redirect('image',tenue_commandee.idtenu)
    return render(request, 'tenue.html', {'commands': commande_instance})

    




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES IMAGES DES TENUES 
# __________________________________________________________________________________________

def modifier_image(request,idmg):
    image_a_modifier=get_object_or_404(ImageModele,idmg=idmg)
    if request.method=="POST":
        image_a_modifier.photos=request.FILES.get("photos")

        if not image_a_modifier.photos:
            messages.error(request, 'Veuiller choisir une image')
            return redirect('modifierImage',idmg=idmg)
        else:
            image_a_modifier.save()
            messages.success(request, 'Image Modifiée avec Succès')
            return redirect('album')
    image_a_afficher=ImageModele.objects.all()
    return render(request, 'modifierImage.html', {'image_a_modifier':image_a_modifier,'image_a_afficher':image_a_afficher})


def supprimer_image(request,idmg):
    image_supp=get_object_or_404(ImageModele,idmg=idmg)
    image_supp.delete()
    messages.warning(request,"image supprimée avec succès")
    return redirect('album')
    


# Permet d'ajouter une image  à la tenue dans la commande
def image(request,idtenu):

    tenue_instance = get_object_or_404(Tenue, idtenu=idtenu)
    if request.method == "POST":
        photos = request.FILES.get("photos")

        if not photos:
            messages.error(request, "Veuillez joindre une image de modele.")
            return redirect('image',idtenu=idtenu)
           
        else:
            
            tenue_avec_image = ImageModele(idtenu=tenue_instance, photos=photos)
            tenue_avec_image.save()
            messages.success(request, 'Image Ajoutée avec Succès, Commande Validée!')
            return redirect('album')
    #Permet d'afficher les tenues avec image
    image_tenue=ImageModele.objects.all()
    return render(request, 'image.html', {'tenue_instance': tenue_instance,'image_tenue':image_tenue})


def infostenue(request,idtenu):
    tenue_instance=get_object_or_404(Tenue,idtenu=idtenu)
    details={
        "tenue_infos":tenue_instance
    }
    
    return render(request,"infosTenue.html",{'details':details})




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES FACTURES
# __________________________________________________________________________________________


def facture(request):
    commandes = Commande.objects.all().order_by('idcom')
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

    # # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all().order_by('idclient')
    facture=Facture.objects.all().order_by('-date_facture')

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'facture.html', {'commandes': commandes, 'clients': clients,'facture':facture})


def createfacture(request):
    commandes = Commande.objects.all().order_by('-idcom')
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

 
    clients = Client.objects.all().order_by('idclient')
    commande_nonfacturee=Commande.objects.filter(facture=None)
    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'creatfacture.html', {'commande_nonfacturee': commande_nonfacturee, 'clients': clients})



def supprimer_facture(request,idfacture):
    factureasupprimer=get_object_or_404(Facture,pk=idfacture)
    factureasupprimer.delete()
    messages.warning(request,"Facture supprimée avec succès")
    return redirect('facture')



def editefacture(request, idcom):
    commande = get_object_or_404(Commande, pk=idcom)
    cle_client = commande.idclient  # Récupération du client lié à la commande
    facture_existante=Facture.objects.filter(idcom=commande).first()

    if facture_existante:
        messages.error(request, "Cette commande a deja une facture.")
        return redirect('facture')
      # Retourne à la page si la date est vide
    elif request.method == "POST":
        date_facture = request.POST.get("date_facture")

        if date_facture == "":
            messages.error(request, "Veuillez entrer la date de facturation.")
            return redirect('editefacture', idcom=idcom)  # Retourne à la page si la date est vide
        else:
            # Création de la facture
            facture = Facture(idclient=cle_client, idcom=commande, date_facture=date_facture)
            facture.save()
            
            messages.success(request, "Facture enregistrée avec succès !")
            # Redirection vers la page d'affichage de la facture avec l'ID de la facture
            return redirect('Aff_Facture', idfacture=facture.idfacture)

    return render(request, 'editefacture.html', {'commande': commande, 'client': cle_client})



def modifier_facture(request,idfacture):
    facture=Facture.objects.select_related('idcom').get(idfacture=idfacture)
    if request.method == "POST":
        facture.idfacture=request.POST.get("idfacture",facture.idfacture)
        facture.idclient=request.POST.get("idclient",facture.idclient)
        facture.idcom=request.POST.get("idcom",facture.idcom)
        facture.idcom.montantcom=request.POST.get("montantcom",facture.idcom.montantcom)
        facture.date_facture = request.POST.get("date_facture",facture.date_facture)

        if facture.date_facture == "":
            messages.error(request, "Veuillez entrer la date de facturation.")
            return redirect('modifierFacture', idfacture=idfacture)  # Retourne à la page si la date est vide
        else:
            facture.save()
            
            messages.success(request, "Facture Modifiée avec succès !")
            # Redirection vers la page d'affichage de la facture avec l'ID de la facture
            return redirect('Aff_Facture', idfacture=facture.idfacture)

    return render(request, 'modifierFacture.html', {'facture': facture})




def Aff_Facture(request,idfacture):
    # Récupérer la facture avec ses détails
    facture = get_object_or_404(Facture, idfacture=idfacture)
    tenues = facture.idcom.tenue_set.all()  # Récupère les tenues de la commande associée

    details = {
        "client": facture.idclient,
        "commande": facture.idcom,
        "tenues": tenues,
        "date_facture": facture.date_facture,
        "total_commande": facture.idcom.montantcom,
    }

    return render(request, 'Aff_Facture.html', {
        'facture': facture,
        'details': details,
    })
    




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES ALBUMS 
# __________________________________________________________________________________________

def album(request):
    #Toutes les qui sont associées à des images
    infosimage=ImageModele.objects.select_related("idtenu").order_by('-ajout')
    return render(request,'album.html',{'infosimage':infosimage})
                







# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES STATISTIQUES
# __________________________________________________________________________________________

def statistique(request):

     # Récupérer les clients ajoutés par semaine
    clients_per_week = Client.objects.annotate(week=TruncWeek('ajout')) \
                                    .values('week') \
                                    .annotate(client_count=Count('idclient')) \
                                    .order_by('week')

    # Extraire les données pour le graphique
    categories = [client['week'].strftime('%d-%m-%Y') for client in clients_per_week]  # Semaine formatée en date
    data = [client['client_count'] for client in clients_per_week]  # Nombre de clients par semaine

    context = {
        'categories': categories,
        'data': data
    }
    return render(request,'statistique.html',context)
   


       
    
    