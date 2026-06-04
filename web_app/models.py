from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=None)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name + " ("+ str(self.flan_uuid)+")"
    
def generate_slug(instance, url=None):
    slug = slugify(instance.name)
    
    if url is not None:
        slug = url

    qs = Flan.objects.filter(slug=slug).order_by("-id")
    
    if qs.exists():
        nuevo_slug = f'{slug}-{qs.first().id}'
        return generate_slug(instance, url=nuevo_slug)
    
    return slug
        
def call_back_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_slug(instance)

pre_save.connect(call_back_pre_save, sender=Flan)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name =  models.CharField(max_length=64)
    message = models.TextField()

class ContactFormModelForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name =  models.CharField(max_length=64)
    message = models.TextField()