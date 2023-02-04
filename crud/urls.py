
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
