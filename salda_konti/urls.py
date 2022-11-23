from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),  
    path('rang_lista_kupci', views.rang_lista_kupci, name='rang_lista_kupci'),
    path('rang_lista_dobavljaci', views.rang_lista_dobavljaci, name='rang_lista_dobavljaci'),
    path('analiza_prosjeka_place', views.analiza_prosjeka_place, name='analiza_prosjeka_place'),
]
