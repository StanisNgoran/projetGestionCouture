# coutureApp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from.models import Client
from.models import Commande
from.models import Tenue
from.models import ImageModele,Facture
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncWeek
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Profil



# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS PRESENTES DANS HOME(MENUE PRINCIPAL) 
# ____________________________________________________________________________________


def inscription(request):
    if request.method=="POST":
        nomUtilisateur=request.POST['username']
        email=request.POST['email']
        motPasse=request.POST['password1']
        motPasseConfirm=request.POST['password2']
        if User.objects.filter(username=nomUtilisateur).exists():
            messages.error(request,"Cet nom utilisateur est deja utilisé")
        elif motPasse!=motPasseConfirm:
            messages.error(request,"Le mot de passe doit etre identique") 
        else:
            
            # creation de l'utilisateur
            utilisateur=User.objects.create_user(username=nomUtilisateur,email=email,password=motPasseConfirm)
            utilisateur.save()

            # Connexion automatique apres creation du compte
            login(request,utilisateur)
            # messages.success(request,"Compte Crée avec succès")
            return redirect('homeUser')
        
    utilisateurs=User.objects.all() 
    return render(request,"authentification/register.html",{'utilisateur':utilisateurs})


def connexion(request):
    if request.method == "POST":
        nomUtilisateur = request.POST["username"]
        motPasse = request.POST["password"]
        utilisateur = authenticate(request, username=nomUtilisateur, password=motPasse)
        if utilisateur:
            login(request, utilisateur)
            # messages.success(request, "Connexion réussie !") 

            # Récupérer le profil de l'utilisateur et vérifier son rôle
            try:
                profil = Profil.objects.get(user=utilisateur)
                if profil.role == "admin":
                    return redirect("home")  # Redirection vers la page admin
                else:
                    return redirect("homeUser")  # Redirection vers la page utilisateur
            except Profil.DoesNotExist:
                messages.error(request, "Votre profil n'existe pas.")

        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'authentification/login.html')



def deconnexion(request):
    logout(request)
    # messages.success(request, "Vous avez été déconnecté.")
    return redirect('login')


@login_required
def listeUtilisateur(request):
    listeUser=Profil.objects.all()
    # listeUser=User.objects.all()
    return render(request,"admin/utilisateur.html",{'utilisateurs':listeUser})

@login_required
def supprimerUtilisateur(request,id):
    idpro=get_object_or_404(Profil,id=id)
    idpro.delete()
    messages.success(request,"Utilisateur Supprimé avec succes")
    return redirect('utilisateur')


@login_required
def modifierUtilisateur(request,id):
    idprofile=get_object_or_404(Profil,id=id)
    if request.method=='POST':
        idprofile.role=request.POST.get("role",idprofile.role)
        if idprofile.role=="":
            messages.error(request,"Changer le role de l'utilisateur")
        else:
            idprofile.save()
            messages.success(request,"Rôle changé avec succes")
    return render(request,"admin/modifierProfile.html",{'listeProfile':idprofile})


@login_required
def creerUtilisateur(request):
    if request.method=="POST":
        nomUtilisateur=request.POST['username']
        email=request.POST['email']
        motPasse=request.POST['password1']
        motPasseConfirm=request.POST['password2']
        if User.objects.filter(username=nomUtilisateur).exists():
            messages.error(request,"Cet nom utilisateur est deja utilisé")
        elif motPasse!=motPasseConfirm:
            messages.error(request,"Le mot de passe doit etre identique") 
        else:
            
            # creation de l'utilisateur
            utilisateur=User.objects.create_user(username=nomUtilisateur,email=email,password=motPasseConfirm)
            utilisateur.save()
            messages.success(request,"Utilisateur crée avec succes")
            return redirect('utilisateur')
    return render (request,"admin/creerUser.html")


@login_required
def home(request):

    # Permet d'afficher toutes les commandes dans un tableau
    # commandes = Commande.objects.all().order_by('-creation')

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'admin/home.html')

@login_required
def homeUser(request):

    # Permet d'afficher toutes les commandes dans un tableau
    # commandes = Commande.objects.all().order_by('-creation')

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'user/homeUser.html')




# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES CLIENTS 
# ____________________________________________________________________________________
# Creation du client



@login_required
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
    return render(request, 'user/client.html')  



# Affiche la liste des clients 

@login_required
def clientlist(request):
    clients=Client.objects.all().order_by('-ajout')
    return render(request,'user/clientlist.html',{'clients':clients})




# Permet de modifier un client 

@login_required
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
    return render(request, 'user/modifierClient.html', {'client': client_a_modifier})



# permet de supprimer un client
 
@login_required
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

# affiche les commandes en cours

@login_required
def commandlist(request):
    commandes=Commande.objects.filter(statut="En Cours").order_by("-creation").all()
    return render(request,'user/commandlist.html',{'commandes':commandes})



# Enregistrement de la commande d'un client donné

@login_required
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
    return render(request, 'user/commande.html', {'client': client_commandeur})




# Permet de modifier une commande

@login_required
def modifier_commande(request,idcom):
    commande_a_modifier= get_object_or_404(Commande,idcom=idcom)
    if request.method=='POST':
        commande_a_modifier.debutcom=request.POST.get('debutcom',commande_a_modifier.debutcom)
        commande_a_modifier.fincom=request.POST.get('fincom',commande_a_modifier.fincom)
        
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
    return render(request,'user/modifierComand.html',{'commande':commande_a_modifier})




@login_required
def infosCommande(request,idcom):
    commande=get_object_or_404(Commande,idcom=idcom)
    tenue_commandee=commande.tenue_set.all()
    details={
        "tenues":tenue_commandee,
        "total_commande":commande.montantcom


    }

    return render(request,"user/infosCommande.html",{'details':details,'commande':commande})



@login_required
def Historique_de_commande(request):
    historique=Commande.objects.filter(statut="Livrée").all()
    return render(request,"user/historiqueCommande.html",{"historique":historique})


@login_required
def Liste_de_retrait(request):
    commandes=Commande.objects.filter(statut="En Cours").order_by("-creation").all()
    return render(request,'user/retraitCommande.html',{'commandes':commandes})



@login_required
def Action_Retrait(request,idcom):
    commande_a_retirer=get_object_or_404(Commande,idcom=idcom)
    if request.method=="POST":
        commande_a_retirer.statut=request.POST.get("statut")
        commande_a_retirer.dateretrait=request.POST.get("dateretrait")

        if commande_a_retirer.statut=="":
            messages.error(request,"Veuillez le statut de la commande!")
            return redirect('actionRetrait',idcom=idcom)
        elif commande_a_retirer.dateretrait=="":
            messages.error(request,"Entrez la date de retrait!")
            return redirect('actionRetrait',idcom=idcom)
        else:
            commande_a_retirer.save()
            messages.success(request,"Retrait Effectuée avec succes!")
            return redirect('HistoriqueCommande')
    return render(request,"user/actionRetrait.html",{'commande_a_retirer':commande_a_retirer})


# Permet de supprimer une commande
@login_required
def supprimer_commande(request,idcom):
    commande=get_object_or_404(Commande,idcom=idcom)
    commande.delete()
    messages.success(request,'Commande supprimée avec succès')
    return redirect('commandlist')







# ____________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES TENUES 
# ____________________________________________________________________________________

@login_required
def Historique_Tenue(request):
    tenue_retiree = Tenue.objects.filter(idcom__statut='Livrée')
    return render(request,'user/historiqueTenue.html',{'tenues':tenue_retiree})



# Permet d'afficher la liste des tenues
@login_required
def listeTenue(request):
    tenues_encours=Tenue.objects.filter(idcom__statut='En Cours').order_by('-ajout')
    return render(request,'user/listeTenue.html',{'tenues':tenues_encours})


# Permet de modifier une tenue 
@login_required
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
    return render(request,"user/modifierTenue.html",{'tenue':tenue})



# Permet de supprimer une tenue dans une commande 
@login_required
def supprimer_tenue(request,idtenu):
    tenue=get_object_or_404(Tenue,pk=idtenu)
    tenue.delete()
    messages.success(request,"Tenue supprimée avec succès")
    return redirect('listeTenue')



# Permet d'enregistrer une tenue dans la commande
@login_required
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
    return render(request, 'user/tenue.html', {'commands': commande_instance})

    




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES IMAGES DES TENUES 
# __________________________________________________________________________________________
@login_required
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
    return render(request, 'user/modifierImage.html', {'image_a_modifier':image_a_modifier,'image_a_afficher':image_a_afficher})

@login_required
def supprimer_image(request,idmg):
    image_supp=get_object_or_404(ImageModele,idmg=idmg)
    image_supp.delete()
    messages.warning(request,"image supprimée avec succès")
    return redirect('album')
    


# Permet d'ajouter une image  à la tenue dans la commande
@login_required
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
    return render(request, 'user/image.html', {'tenue_instance': tenue_instance,'image_tenue':image_tenue})



@login_required
def infostenue(request,idtenu):
    tenue_instance=get_object_or_404(Tenue,idtenu=idtenu)
    details={
        "tenue_infos":tenue_instance
    }
    
    return render(request,"user/infosTenue.html",{'details':details})




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES FACTURES
# __________________________________________________________________________________________

@login_required
def facture(request):
    commandes = Commande.objects.all().order_by('idcom')
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

    # # permet de remplir le comboBox des ID du client 
    clients = Client.objects.all().order_by('idclient')
    facture=Facture.objects.all().order_by('-date_facture')

    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'user/facture.html', {'commandes': commandes, 'clients': clients,'facture':facture})



@login_required
def createfacture(request):
    commandes = Commande.objects.all()
    for commande in commandes :
        commande.nombre_tenue=commande.calculer_NombreTenue()

    commande_nonfacturee=Commande.objects.filter(facture=None).order_by('-creation')
    # Retourne les commandes et clients dans le contexte du template
    return render(request, 'user/creatfacture.html', {'commande_nonfacturee': commande_nonfacturee})


@login_required
def supprimer_facture(request,idfacture):
    factureasupprimer=get_object_or_404(Facture,pk=idfacture)
    factureasupprimer.delete()
    messages.warning(request,"Facture supprimée avec succès")
    return redirect('facture')


@login_required
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

    return render(request, 'user/editefacture.html', {'commande': commande, 'client': cle_client})


@login_required
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

    return render(request, 'user/modifierFacture.html', {'facture': facture})



@login_required
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

    return render(request, 'user/Aff_Facture.html', {
        'facture': facture,
        'details': details,
    })
    




# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES OPERATIONS A EFFECTUER SUR LES ALBUMS 
# __________________________________________________________________________________________
@login_required
def album(request):
    #Toutes les qui sont associées à des images
    infosimage=ImageModele.objects.select_related("idtenu").order_by('-ajout')
    return render(request,'user/album.html',{'infosimage':infosimage})
                







# __________________________________________________________________________________________
#  CETTE PARTIE DU CODE CONCERNE TOUTES LES STATISTIQUES
# __________________________________________________________________________________________
@login_required
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
   


       
    
    