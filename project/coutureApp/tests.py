from django.test import TestCase
from django.urls import reverse
from coutureApp.models import Client

class AjouterClientTest(TestCase):

    def test_client_enregistrement_succes(self):
        
        #Vérifie qu'un client est bien enregistré si toutes les conditions sont respectées.
       
        response = self.client.post(reverse('client'), {
            'nom': 'DUPONT',
            'prenom': 'JEAN',
            'contact': '0123456789'
        })

        # Vérifier si le client a bien été créé
        self.assertEqual(Client.objects.count(), 1)
        client = Client.objects.first()
        self.assertEqual(client.nom, 'DUPONT')
        self.assertEqual(client.prenom, 'JEAN')
        self.assertEqual(client.contact, '0123456789')

        # Vérifie la redirection après ajout
        self.assertRedirects(response, reverse('clientlist'))

    def test_client_nom_vide(self):
    
        #Vérifie que l'ajout échoue si le nom est vide.
        
        response = self.client.post(reverse('client'), {
            'nom': '',
            'prenom': 'JEAN',
            'contact': '0123456789'
        })

        # Aucun client ne doit être créé
        self.assertEqual(Client.objects.count(), 0)

        # Vérifier que le message d'erreur est bien affiché
        self.assertContains(response, "Veuillez Entrer le nom du client.")

    def test_client_prenom_vide(self):
        
        #Vérifie que l'ajout échoue si le prénom est vide.
        
        response = self.client.post(reverse('client'), {
            'nom': 'DUPONT',
            'prenom': '',
            'contact': '0123456789'
        })

        self.assertEqual(Client.objects.count(), 0)
        self.assertContains(response, "Veuillez Entrer le prenom du client.")

    def test_client_contact_vide(self):
    
        #Vérifie que l'ajout échoue si le contact est vide.
        
        response = self.client.post(reverse('client'), {
            'nom': 'DUPONT',
            'prenom': 'JEAN',
            'contact': ''
        })

        self.assertEqual(Client.objects.count(), 0)
        self.assertContains(response, "Veuillez saisir le contact.")

    def test_client_contact_invalide(self):
    
        #Vérifie que l'ajout échoue si le contact n'est pas valide (pas 10 chiffres).
    
        response = self.client.post(reverse('client'), {
            'nom': 'DUPONT',
            'prenom': 'JEAN',
            'contact': '1234'  # Mauvais format
        })

        self.assertEqual(Client.objects.count(), 0)
        self.assertContains(response, "Le contact doit etre 10 chiffres.")
