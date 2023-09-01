from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppTickets.forms import ArtistForm, EventForm, ClientForm, RegistroUsuariosForm, \
                             UserEditForm, AvatarFormulario, FormularioCambioPassword

from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.views import PasswordChangeView #,LoginView

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

# Create your views here.
def home(request):
    return render(request, "AppTickets/home.html")

def about_me(request):
    return render(request, "AppTickets/about_me.html")

@login_required
def events(request):
    contexto = {'eventos': Event.objects.all()}
    return render(request, "AppTickets/events.html", contexto)

@login_required
def artists(request):
    contexto = {'artistas': Artist.objects.all()}
    return render(request, "AppTickets/artists.html", contexto)

@login_required
def clients(request):
    contexto = {'clientes': Client.objects.all()}
    return render(request, "AppTickets/clients.html", contexto)

@login_required
def artistForm(request): 
    if request.method == "POST":
        miForm = ArtistForm(request.POST) # info comes from the html
        if miForm.is_valid():
            artist_name = miForm.cleaned_data.get('name')
            artist_webpage = miForm.cleaned_data.get('webpage')
            artist = Artist(name=artist_name, webpage=artist_webpage)
            artist.save()
            return render(request, "AppTickets/base.html")
    else: # if first time called
        miForm = ArtistForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/artistForm.html", contexto)

@login_required
def search_(request):
    if request.GET['search']:
        pattern = request.GET['search']
        artistas_ = Artist.objects.filter(name__icontains=pattern)
        contexto = {"artistas": artistas_, 'title': f'Artists containing the pattern "{pattern}"'}
        return render(request, "AppTickets/artists.html", contexto)
    return HttpResponse("Please, indicate a pattern to be searched")

@login_required
def artistSearch(request):
    return render(request, "AppTickets/artistSearch.html")


@login_required
def eventForm(request): 
    if request.method == "POST":
        miForm = EventForm(request.POST) # info comes from the html
        if miForm.is_valid():
            event_name_in = miForm.cleaned_data.get('event_name')
            artist_in = miForm.cleaned_data.get('artist')
            country_in = miForm.cleaned_data.get('country')
            city_in = miForm.cleaned_data.get('city')
            venue_in = miForm.cleaned_data.get('venue')
            date_in = miForm.cleaned_data.get('date')
            soldOut_in = False #miForm.cleaned_data.get('sold_out')
            event_in = Event(event_name=event_name_in, artist=artist_in,
                             country=country_in, city=city_in, venue=venue_in,
                             date=date_in, soldOut=soldOut_in)
            event_in.save()
            return render(request, "AppTickets/base.html")
    else: # if first time called
        miForm = EventForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/eventForm.html", contexto)

@login_required
def clientForm(request): 
    if request.method == "POST":
        miForm = ClientForm(request.POST) # info comes from the html
        if miForm.is_valid():
            client_name_in = miForm.cleaned_data.get('name')
            client_surname_in = miForm.cleaned_data.get('surname')
            client_email_in = miForm.cleaned_data.get('email')
            client_in = Client(firstName=client_name_in, lastName=client_surname_in,
                             email=client_email_in)
            client_in.save()
            return render(request, "AppTickets/clients.html")
    else: # if first time called
        miForm = ClientForm()
    contexto = {"form": miForm }
    return render(request, "AppTickets/clientForm.html", contexto)

#______________________________________________________________
# CRUD for Client model
class ClientList(LoginRequiredMixin, ListView):
    model = Client

class ClientCreate(SuperUserRequiredMixin, CreateView):
    model = Client
    fields = ['firstName', 'lastName', 'email']
    success_url = reverse_lazy('clientes')

class ClientUpdate(SuperUserRequiredMixin, UpdateView):
    model = Client
    fields = ['firstName', 'lastName', 'email']
    success_url = reverse_lazy('clientes')

class ClientDelete(SuperUserRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clientes')

#______________________________________________________________
# CRUD for Venue model
class VenueList(LoginRequiredMixin, ListView):
    model = Venue

class VenueCreate(SuperUserRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'country', 'city', 'address', 'webpage']
    success_url = reverse_lazy('lugares')

class VenueUpdate(SuperUserRequiredMixin, UpdateView):
    model = Venue
    fields = ['name', 'country', 'city', 'address', 'webpage']
    success_url = reverse_lazy('lugares')

class VenueDelete(SuperUserRequiredMixin, DeleteView):
    model = Venue
    success_url = reverse_lazy('lugares')

#______________________________________________________________
# CRUD for Artist model
class ArtistList(LoginRequiredMixin, ListView):
    model = Artist

class ArtistCreate(SuperUserRequiredMixin, CreateView):
    model = Artist
    fields = ['name', 'webpage']
    success_url = reverse_lazy('artistas')

class ArtistUpdate(SuperUserRequiredMixin, UpdateView):
    model = Artist
    fields = ['name', 'webpage']
    success_url = reverse_lazy('artistas')

class ArtistDelete(SuperUserRequiredMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('artistas')

#______________________________________________________________
# CRUD for Event model
class EventList(LoginRequiredMixin, ListView):
    model = Event

class EventCreate(SuperUserRequiredMixin, CreateView):
    model = Event
    #fields = ['event_name', 'artist', 'country', 'city', 'venue', 'date', 'soldOut']
    fields = ['event_name', 'artist', 'venue', 'date', 'soldOut']
    success_url = reverse_lazy('eventos')

class EventUpdate(SuperUserRequiredMixin, UpdateView):
    model = Event
    #fields = ['event_name', 'artist', 'country', 'city', 'venue', 'date', 'soldOut']
    fields = ['event_name', 'artist', 'venue', 'date', 'soldOut']
    success_url = reverse_lazy('eventos')

class EventDelete(SuperUserRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('eventos')

@login_required
def search_event(request):
    if request.GET['search']:
        pattern = request.GET['search']
        eventos_ = Event.objects.filter(event_name__icontains=pattern)
        contexto = {"eventos": eventos_, 'title': f'Events whose name contains the pattern "{pattern}"'}
        return render(request, "AppTickets/events.html", contexto)
    return HttpResponse("Please, indicate a pattern to be searched")

def welcome(request):
    return render(request, 'AppTickets/welcome.html', {})

@login_required
def eventSearch(request):
    return render(request, "AppTickets/event_search.html")
#______________________________________________________________

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/image_default.jpg"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "AppTickets/welcome.html", {'mensaje': f'Welcome to WorldTickets {usuario}'})
            else:
                return render(request, "AppTickets/login.html", {'form': miForm, 'mensaje': f'Invalid data'})
        else:
            return render(request, "AppTickets/login.html", {'form': miForm, 'mensaje': f'Invalid data'})

    miForm = AuthenticationForm()

    return render(request, "AppTickets/login.html", {"form":miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "AppTickets/signupExitoso.html")
    else:
        miForm = RegistroUsuariosForm()      
    return render(request, "AppTickets/register.html", {"form":miForm})

def signup_exitoso(request):
    return render(request, 'AppTickets/signupExitoso.html', {})

#_______________________________________________________________________________________________

"""
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            #usuario.password1 = form.cleaned_data.get('password1')
            #usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"AppTickets/base.html")
        else:
            return render(request,"AppTickets/editProfile.html", {'form': form, 'usuario': usuario.username})
    else: # invalid data
        form = UserEditForm(instance=usuario)
    return render(request, "AppTickets/editProfile.html", {'form': form, 'usuario': usuario.username})
"""
#________________________________________________________________
class editProfile(UpdateView):
    form_class = UserEditForm
    template_name= 'AppTickets/editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppTickets/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'AppTickets/passwordExitoso.html', {})


#__________________________________________________________________

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"AppTickets/home.html")
    else:
        form = AvatarFormulario()
    return render(request, "AppTickets/addAvatar.html", {'form': form })

#_______________________________________
def user_detail(request):
  user_detail = request.user.objects.filter(id=id)
  return(request,'user_datail.html',{'user_detail':user_detail})