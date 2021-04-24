from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('jwt-auth/', obtain_jwt_token),
    path('jwt-refresh/', refresh_jwt_token),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', views.schema_view.without_ui(cache_timeout = 0), name = 'schema-json'),
    re_path(r'swagger/$', views.schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    re_path(r'^redoc/$', views.schema_view.with_ui('redoc', cache_timeout = 0), name = 'schema-redoc'),
]
