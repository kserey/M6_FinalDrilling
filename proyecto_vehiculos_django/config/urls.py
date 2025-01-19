from django.contrib import admin
from django.urls import path, include
from vehiculo.views import index
from django.contrib.auth import views as auth_views
from vehiculo.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("vehiculo/", include("vehiculo.urls")),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
