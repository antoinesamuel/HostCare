from django.shortcuts import render
from gestion_consultation.models import Consultation, Medecine_generale, Ophtalmologie
from gestion_consultation.services import create_Consultation


# Create your views here.


def creerConsultation(request):
    # La vue ne fait que recevoir les données et appeler le service
    if request.method == "POST":
        donnees = request.POST
        create_Consultation(donnees)
        return "hello"

