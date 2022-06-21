from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


router = DefaultRouter()
router.register(r'questionpaper', views.QuestionPaperViewSet, basename='questionpaper')
router.register(r'rawquestion', views.RawQuestionViewSet, basename='rawquestion')
router.register(r'questionset', views.QuestionSetViewSet, basename='questionset')
router.register(r'exportdoc', views.ExportDocViewSet, basename='exportdoc')



urlpatterns = [
    path('', include(router.urls)),
    # path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('exportdoc/', views.ExportDocViewSet.as_view({'get': 'list'}), name='exportdoc'),
    ]
