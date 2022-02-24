from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import OfferViewSet, specialite_list, cv_list, cv_detail, resume_list, offreDetail, CandViewSet

router = routers.DefaultRouter()
router.register(r'offre', OfferViewSet)
router.register(r'cand', CandViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('specialite/',specialite_list),
    path('candidat/<str:category>/',cv_list),
    path('candidat/<str:category>/<int:id>/',cv_detail),
    path('candidat/',resume_list),
    path('offr/<int:id>/',offreDetail),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
