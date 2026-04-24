from django.db import models

# Create your models here.
class Consultation (models.Model):
    patient = models.ForeignKey('gestion_users.Patient', on_delete=models.CASCADE)
    medecin = models.ForeignKey('gestion_users.Medecin', on_delete=models.CASCADE)
    date_consultation = models.DateTimeField()

    
    
    def __str__(self):
        return f"Consultation de {self.patient} avec {self.medecin} le {self.date_consultation}"