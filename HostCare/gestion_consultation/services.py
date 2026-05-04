from gestion_consultation.models import Consultation, Medecine_generale, Ophtalmologie


#Afficher Toutes les Consultations


#Creer une Consultation
def create_Consultation(consultation):
        consultation=Consultation.creates()
        consultation.save()