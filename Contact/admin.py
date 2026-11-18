from django.contrib import admin
from .models import ContactData, Social, Private, Impressum, Agb, Logo, ContactForm, ContactFormThanks
# Register your models here.
admin.site.register(ContactData)
admin.site.register(Social)
admin.site.register(Private)
admin.site.register(Impressum)
admin.site.register(Agb)
admin.site.register(Logo)

admin.site.register(ContactForm)
admin.site.register(ContactFormThanks)