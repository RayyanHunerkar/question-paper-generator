from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_nested import routers
from django.urls import path, include, re_path
from . import views


router = DefaultRouter(trailing_slash=False)
# router.register(r'rawquestion', views.RawQuestionViewSet, basename='rawquestion')
router.register(r'questionpaper', views.QuestionPaperViewSet, basename='questionpaper')

questionset_router = routers.NestedSimpleRouter(router, r'questionpaper', lookup='questionpaper')
questionset_router.register(r'questionset', views.QuestionSetViewSet, basename='questionset')

question_router = routers.NestedSimpleRouter(questionset_router, r'questionset', lookup='questionset')
question_router.register(r'question', views.QuestionViewSet, basename='question')

exportdoc_router = routers.NestedSimpleRouter(question_router, r'question', lookup='question')
exportdoc_router.register(r'exportdoc', views.ExportDocViewSet, basename='exportdoc')

app_name = 'questionpaper'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(questionset_router.urls)),
    path('', include(question_router.urls)),
    path('', include(exportdoc_router.urls)),
    ]
