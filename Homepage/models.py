from django.db import models
from django import forms
from django.contrib import admin
from ckeditor.fields import RichTextField

# Create your models here.
class Intro(models.Model):
    img1 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='zdjęcie 1')
    title = models.TextField(null=True, blank=True, verbose_name='tytuł w sekcji hero')





    
    

    class Meta:
        """Meta definition for intro."""

        verbose_name = 'Pierwsza sekcja na stronie głównej '
        verbose_name_plural = 'Pierwsza sekcja na stronie głównej '

    def __str__(self):
         return f'Kliknij aby modyfikować pierwszą sekcję na stronie'
    def clean(self):
            if not self.pk and Intro.objects.exists():
                raise forms.ValidationError('Nie można utworzyć więcej niż jednej instancji modelu.')
            return super().clean()


