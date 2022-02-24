from django.db import models
from djongo.models import json
from rest_framework.fields import ListField


class Offre(models.Model):
    Name = models.CharField(max_length=1000)
    StartDate = models.DateField(max_length=50)
    EndDate = models.DateField(max_length=50)
    Description = models.CharField(max_length=100000, null=True, blank=True)

    def __str__(self):
        return self.Name


class Specialite(models.Model):
    Category = models.CharField(max_length=30)
    NumberCv = models.IntegerField()

    def __str__(self):
        return self.NameSpecialite


class NumberCv(models.Model):
    Category = models.CharField(max_length=30)
    NumberCv = models.IntegerField()

    def __str__(self):
        return self.NumberCv


class Candidat(models.Model):
    id = models.IntegerField(primary_key=True)
    Names = models.CharField(max_length=100)
    Category = models.CharField(max_length=30)
    Phones = models.CharField(max_length=200)

    def set_phones(self, x):
        self.Phones = json.dumps(x)

    def get_phones(self):
        return json.loads(self.Phones)

    Emails = models.CharField(max_length=200)

    def set_emails(self, x):
        self.emails = json.dumps(x)

    def get_emails(self):
        return json.loads(self.emails)
    Path=models.CharField(max_length=1000)


class Cv(models.Model):
    id = models.IntegerField(primary_key=True)
    Names = models.CharField(max_length=100, null=True)
    Phones = models.CharField(max_length=200)

    def set_phones(self, x):
        self.Phones = json.dumps(x)

    def get_phones(self):
        return json.loads(self.Phones)

    Emails = models.CharField(max_length=200)

    def set_emails(self, x):
        self.emails = json.dumps(x)

    def get_emails(self):
        return json.loads(self.emails)

    Degrees = models.CharField(max_length=100)
    Diplomes = models.CharField(max_length=200)

    def set_diplomes(self, x):
        self.Diplomes = json.dumps(x)

    def get_diplomes(self):
        return json.loads(self.Diplomes)

    Universities = models.CharField(max_length=1000)

    def set_universities(self, x):
        self.Universities = json.dumps(x)

    def get_universities(self):
        return json.loads(self.Universities)

    Skills = models.CharField(max_length=200)

    def set_skills(self, x):
        self.Skills = json.dumps(x)

    def get_skills(self):
        return json.loads(self.Skills)

    Interests = models.CharField(max_length=1000)

    def set_interests(self, x):
        self.Interests = json.dumps(x)

    def get_interests(self):
        return json.loads(self.Interests)

    Languages = models.CharField(max_length=1000)

    def set_languages(self, x):
        self.Languages = json.dumps(x)

    def get_languages(self):
        return json.loads(self.Languages)

    Categories = models.CharField(max_length=30, null=True)
    Postes = models.CharField(max_length=1000)

    def set_postes(self, x):
        self.Postes = json.dumps(x)

    def get_postes(self):
        return json.loads(self.Postes)

    Entreprises = models.CharField(max_length=1000)

    def set_entreprises(self, x):
        self.Entreprises = json.dumps(x)

    def get_entreprises(self):
        return json.loads(self.Entreprises)

    Content = models.CharField(max_length=1000000, null=True)
    Path= models.CharField(max_length=1000)


class Resume(models.Model):
    id = models.IntegerField(primary_key=True)
    Content = models.CharField(max_length=1000000)
    Names = models.CharField(max_length=100)
    Phones = models.CharField(max_length=100)

    def set_phones(self, x):
        self.Phones = json.dumps(x)

    def get_phones(self):
        return json.loads(self.Phones)

    Emails = models.CharField(max_length=200)

    def set_emails(self, x):
        self.emails = json.dumps(x)

    def get_emails(self):
        return json.loads(self.emails)

    Degrees = models.CharField(max_length=100)
    Diplomes = models.CharField(max_length=200)

    def set_diplomes(self, x):
        self.Diplomes = json.dumps(x)

    def get_diplomes(self):
        return json.loads(self.Diplomes)

    Skills = models.CharField(max_length=200)

    def set_skills(self, x):
        self.Skills = json.dumps(x)

    Universities = models.CharField(max_length=1000)

    def set_universities(self, x):
        self.Universities = json.dumps(x)

    def get_universities(self):
        return json.loads(self.Universities)

    def get_skills(self):
        return json.loads(self.Skills)

    Interests = models.CharField(max_length=1000)

    def set_interests(self, x):
        self.Interests = json.dumps(x)

    def get_interests(self):
        return json.loads(self.Interests)

    Languages = models.CharField(max_length=1000)

    def set_languages(self, x):
        self.Languages = json.dumps(x)

    def get_languages(self):
        return json.loads(self.Languages)

    Categories = models.CharField(max_length=30, null=True)
    Postes = models.CharField(max_length=1000)

    def set_postes(self, x):
        self.Postes = json.dumps(x)

    def get_postes(self):
        return json.loads(self.Postes)

    Entreprises = models.CharField(max_length=1000)

    def set_entreprises(self, x):
        self.Entreprises = json.dumps(x)

    def get_entreprises(self):
        return json.loads(self.Entreprises)
    Path=models.CharField(max_length=1000)


class Cand(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=1000)
    cv = models.CharField(max_length=1000)
