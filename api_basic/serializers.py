from rest_framework import serializers
from .models import Offre, Specialite, Cv, Candidat, Resume, Cand


class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ['id', 'Name', 'StartDate', 'EndDate','Description']
class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = ['id', 'Category', 'NumberCv']

class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ['id','Names','Category','Phones','Emails','Path']

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = ['id','Names','Phones','Emails','Degrees','Diplomes','Universities','Skills','Interests','Languages','Categories','Postes','Entreprises','Content','Path']
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id','Content','Names','Phones','Emails','Degrees','Diplomes','Universities','Skills','Interests','Languages','Categories','Postes','Entreprises','Path']





class CandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cand
        fields=['id','nom','phone','email','cv']
