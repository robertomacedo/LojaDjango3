from django.urls import path 
from .views import *


app_name = "ldjango"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]