
from . import views 
import connexion.views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index' ),
    path('signup/',connexion.views.signup_page,name='signup'),
]
