from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r'questionpaper', views.QuestionPaperViewSet, basename='questionpaper')
router.register(r'rawquestion', views.RawQuestionViewSet, basename='rawquestion')

urlpatterns = [
    path('', include(router.urls)),
    ]
