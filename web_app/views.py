from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from web_app.forms import ContactoForm, ContactFormForm, CustomUserCreationForm, FlanFormForm
from web_app.models import Flan, ContactFormModelForm, ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request=request, template_name='index.html', context={'flanes_publicos':flanes_publicos})

def acerca(request):
    return render(request=request, template_name='about.html', context={})

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request=request, template_name='welcome.html', context={'flanes_privados':flanes_privados})

def base(request):
    return render(request=request, template_name='contenedor.html', context={})

def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactFormForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return render(request, "custom/mensaje.html", {"mensaje":"Gracias por contactarte con OnlyFlans, te responderemos en breve"})

    contacto_form = ContactFormForm()
    return render(request, "contacto.html", { 'form':contacto_form })

def registro_flanes(request):
    if request.method == 'POST':
        flan_form = FlanFormForm(request.POST)
        print(f'flan_form: {flan_form}')
        if flan_form.is_valid():
            flan_form.save()
            return render(request, "custom/mensaje.html", {"mensaje":"Flan guardado con éxito"})
        
    flan_form = FlanFormForm()
    #return render(request, "registro_flanes.html", { 'form':flan_form })
    return render(request, "custom/mensaje.html", {"mensaje":"Flan registrado con éxito"}, { 'form':flan_form })

def contacto2(request):
    if request.method == 'POST':
        contacto_form = ContactFormModelForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return render(request, "custom/mensaje.html", {"mensaje":"Gracias por contactarte con OnlyFlans, te responderemos en breve"})
    
    contacto_form = ContactFormModelForm()
    return render(request, "contacto.html", { 'form':contacto_form })
    
def obtener_flanes(request):
    flanes = Flan.objects.all()
    return render(request, "index.html", {'flanes': flanes})

def salir(request):
    logout(request)
    return redirect('/')

def register(request):
    data = {"form": CustomUserCreationForm()}
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            #user_creation_form.save()
            #user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            #login(request=user)
            #return redirect("/")
            return render(request, "custom/mensaje.html", {"mensaje":"Gracias por registrarte a OnlyFlans"})
        
    return render(request, "registration/register.html", data)
