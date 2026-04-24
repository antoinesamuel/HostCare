from django.db import models

# Create your models here.

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=20)
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.specialite}"