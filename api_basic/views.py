import string

import gridfs
from django import db
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser

from rest_framework import viewsets
from unicodedata import category

from .models import Offre, Specialite, Cv, Candidat, Resume, Cand
from .serializers import OffreSerializer, SpecialiteSerializer, CvSerializer, \
    CandidatSerializer, ResumeSerializer, CandSerializer
from pymongo import MongoClient
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import math
from collections import Counter

stop = set(stopwords.words('french', 'english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()

    serializer_class = OffreSerializer


my_client = MongoClient('localhost', 27017)
db = my_client["Resume"]
'''
db1=my_client["ResumeDataset"]
name="( ID 11184) 2019-01-04- 07 - Mohamed Wael Ghannem- ISI 2018.pdf"
file_location="C://Users//Rihab//Desktop//"+ name
file_data=open(file_location,"rb")
data=file_data.read()
fs=gridfs.GridFS(db1)
fs.put(data,filename=name)
print("upload complete")
data=db1.fs.files.find_one({'filename':name})
my_id=data['_id']
outputdata=fs.get(my_id).read()
download_location="C://Users//Rihab//Downloads//"+name
output=open(download_location,"wb")
output.write(outputdata)
output.close()
print("download complete")
'''


def offreDetail(request, id):
    queryset = Offre.objects.filter(id=id)

    if request.method == "GET":
        serializer = OffreSerializer(queryset, many=True)
        cv = []
        for i in range(len(score(id))):
            queryResume = Resume.objects.filter(id=score(id)[i][0]).first()
            cv.append(queryResume)
        ser = ResumeSerializer(cv, many=True)

        cv.append(ser.data)

        res = {}
        res['offre'] = serializer.data

        res['top 10'] = ser.data
        res['score'] = [score(id)[i] for i in range(10)]
        return JsonResponse(res, safe=False)


def specialite_list(request):

    # Aggregation
    cursor = db["api_basic_specialite"].aggregate([{"$group":
                                                        {"_id": "$Category",
                                                         "total collections": {"$sum": 1}
                                                         }
                                                    }])

    a = []
    for document in cursor:
        a.append(document)

    if request.method == "GET":
        specialites = [{'Category': a[i]['_id'], 'NumberCv': a[i]['total collections']} for i in range(len(a) - 1)]

        serializer = SpecialiteSerializer(specialites, many=True)
        return JsonResponse(serializer.data, safe=False)

def cv_list(request, category):
    queryset =Candidat.objects.filter(Category=category)
    if request.method == "GET":
        serializer = CandidatSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

def cv_detail(request, category, id):
    queryset1 = Cv.objects.filter(Categories=category).filter(id=id)
    if request.method == "GET":
        serializer = CvSerializer(queryset1, many=True)
        return JsonResponse(serializer.data, safe=False)


def resume_list(request):
    queryset = Resume.objects.all()
    if request.method == "GET":
        serializer = ResumeSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


def score(idOffre):
    def clean(doc):
        text = re.sub('[^a-zàâçéèêëîïôûùüÿñæœ]', ' ', doc.lower())
        stop_free = " ".join([i for i in text.split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    WORD = re.compile(r'\w+')

    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
        sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator


    cleaned_offre = clean(list(Offre.objects.all().filter(id=idOffre).values('Description'))[0]['Description'])


    resume = []
    for id in range(1, Resume.objects.all().count()+1 ):
        cleaned_resume = clean(list(Resume.objects.all().filter(id=id).values('Content'))[0]['Content'])
        resume.append(cleaned_resume)

    scores = []
    for j in range(len(resume)):
        b = (j + 1, get_cosine(text_to_vector(resume[j]), text_to_vector(cleaned_offre)))
        scores.append(b)

    for i in range(len(scores)):
        scores.sort(key=lambda x: x[1], reverse=True)

    top_10 = []
    for i in range(10):
        top_10.append(scores[i])

    return top_10
class CandViewSet(viewsets.ModelViewSet):
    queryset = Cand.objects.all()

    serializer_class = CandSerializer
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    def post(self,requests,*args,**kwargs):
        print(requests)
        nom=requests.data['nom']
        phone=requests.data['phone']
        email=requests.data['email']
        cv=requests.data['cv']

        Cand.objects.create(nom='nom',phone='phone',email='email',cv='cv')
        return HttpResponse({requests},status=200)
