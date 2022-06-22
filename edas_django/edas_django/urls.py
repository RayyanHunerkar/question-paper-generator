
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="EDAS API",
      default_version='v1',
      description="API Documentation for the base Question Paper Generator",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rayyan.hunerkar@parrkeighteen.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('api.urls')),
    # swagger UI url
   #  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('cached/swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='cschema-swagger-ui'),
   path('cached/redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),

]
