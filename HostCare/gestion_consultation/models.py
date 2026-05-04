from django.db import models

# Create your models here.
class Consultation (models.Model):
    patient = models.ForeignKey('gestion_users.Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey('gestion_users.Medecin', on_delete=models.CASCADE)
    date_consultation = models.DateTimeField()
    antecedents=models.CharField(max_length=500, default='')
    motif_consultation=models.CharField(max_length=500, default='')
    
    
    

class Medecine_generale(Consultation):
        poids = models.FloatField()
        taille= models.FloatField()
        temperature = models.FloatField()
        IMC=models.FloatField()
        diagnostic=models.CharField(max_length=500, default='')
        traitement_en_cours=models.CharField(max_length=500, default='')

        def __str__(self):
         return f"Consultation de {self.patient} avec {self.medecin} le {self.date_consultation}"
    

class Ophtalmologie(Consultation):
        vision_OG=models.CharField(max_length=500, default='')
        vision_OD=models.CharField(max_length=500, default='')
        tension=models.CharField(max_length=500, default='')
        refraction=models.CharField(max_length=500, default='')
    
        def __str__(self):
         return f"Consultation de {self.patient} avec {self.medecin} le {self.date_consultation}"
    

       
     

     
