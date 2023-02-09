
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
