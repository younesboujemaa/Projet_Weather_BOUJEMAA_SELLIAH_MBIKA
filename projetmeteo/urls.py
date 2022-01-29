
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
import connexion.views
import home.views
from projetmeteo import views
from django.conf.urls import handler404,handler500

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('home.urls')),
    path('home/', home.views.index, name='index'),
    path('error/',views.error_404,name='error'),
    path('errror/',views.error_500,name='errror'),
    path('login/', connexion.views.login_page, name='login'),
    path('logout/', connexion.views.logout_user, name='logout'),
    path('signup/',connexion.views.signup_page, name='signup'),
    path('connexion/pageutilisateur',connexion.views.utilisateur_page, name='pageutilisateur'),

]