from django import forms
from django.forms import ModelForm
from web_app.models import ContactForm, Flan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactFormForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message'] 
form = ContactFormForm()

class FlanFormForm(ModelForm):
    class Meta:
        model = Flan
        fields = ['flan_uuid', 'name', 'description', 'image_url', 'slug', 'is_private'] 
form = FlanFormForm()

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=150, label='Apellido')
    email = forms.EmailField(help_text="Ej: a@b.com", label='Email')
    fec_nac = forms.DateField(help_text="yyyy-mm-dd", label='Fecha de Nacimiento')
    comentario = forms.CharField(widget=forms.Textarea({"size": 100}), label="Comentario")
    
# class ContactForm(ModelForm):
#     customer_email = forms.EmailField(help_text="Ej: a@b.com", label='Email', widget=forms.TextInput(attrs={'placeholder': 'Indique su Email'}))
#     customer_name = forms.CharField(max_length=64, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Indique su nombre'}))
#     message = forms.CharField(widget=forms.Textarea({"size": 100}), label="Mensaje")

# contactForm = ContactForm.objects.get(pk=1)
# form = ContactFormModelForm(instance=ContactForm)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
form = CustomUserCreationForm()
