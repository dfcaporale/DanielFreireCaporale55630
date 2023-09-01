from django.urls import path
from AppTickets import views

from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home" ),
    path('about_me/', views.about_me, name="acerca_de_mi" ),
    path('welcome_message/' , views.welcome, name='welcome_message'),

    #path('events/', views.events, name="eventos" ),
    #path('artists/', views.artists, name="artistas" ),
    #path('clients/', views.clients, name="clientes" ),
    
    #path('artist_form/', views.artistForm, name="add_artist_form" ),
    
    path('search_/', views.search_, name="search_" ), #event search
    path('artist_search/', views.artistSearch, name="busca_artista" ), # artist search

    #path('event_form/', views.eventForm, name="add_event_form" ),

    #path('new_client/', views.clientForm, name="new_client_form" ),

    path('clients/', ClientList.as_view(), name="clientes" ),
    path('create_client/', ClientCreate.as_view(), name="create_cliente" ),    
    path('update_client/<int:pk>/', ClientUpdate.as_view(), name="update_cliente" ),
    path('delete_client/<int:pk>/', ClientDelete.as_view(), name="delete_cliente" ),

    path('venues/', VenueList.as_view(), name="lugares" ),
    path('create_venue/', VenueCreate.as_view(), name="create_lugar" ),    
    path('update_venue/<int:pk>/', VenueUpdate.as_view(), name="update_lugar" ),
    path('delete_venue/<int:pk>/', VenueDelete.as_view(), name="delete_lugar" ),

    path('artists/', ArtistList.as_view(), name="artistas" ),
    path('create_artist/', ArtistCreate.as_view(), name="create_artista" ),    
    path('update_artist/<int:pk>/', ArtistUpdate.as_view(), name="update_artista" ),
    path('delete_artist/<int:pk>/', ArtistDelete.as_view(), name="delete_artista" ),

    path('events/', EventList.as_view(), name="eventos" ),
    path('create_event/', EventCreate.as_view(), name="create_evento" ),    
    path('update_event/<int:pk>/', EventUpdate.as_view(), name="update_evento" ),
    path('delete_event/<int:pk>/', EventDelete.as_view(), name="delete_evento" ),

    path('search_event/', views.search_event, name="search_event" ),
    path('event_search/', views.eventSearch, name="busca_evento" ),

    #_________________________________________________
    path('login/', login_request, name="client_login" ),
    path('logout/', LogoutView.as_view(template_name="AppTickets/logout.html"), name="client_logout" ),
    
    path('register/', register, name="client_register" ),
    path('signupExitoso/' , views.signup_exitoso, name='signup_exitoso'),

    #_________________________________________________
    path('edit_perfil/', editProfile.as_view(), name="edit_profile" ),
    path('agregar_foto/', agregarAvatar, name="add_avatar" ),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    #_____________________

]