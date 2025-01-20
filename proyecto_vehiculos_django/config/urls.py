from django.contrib import admin
from django.urls import path, include
from vehiculo.views import index, register, listado
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("vehiculo/", include("vehiculo.urls")),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('listado/', listado, name='listado'), 
]
