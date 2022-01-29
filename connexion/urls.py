from django.urls import path
from . import views 
from django.views.generic.simple import redirect_to
from django.conf.urls import handler404,handler500
from home import views
from pageutilisateur import views


urlpatterns = [
    path('login/', views.login_page, name='login' ),
    path('logout/',connexion.views.logout_user, name='logout'),
    path('pageutilisateur/', views.utilisateur_page,name='pageutilisateur'),
    path('home/', home.views.index, name='index'),
]

