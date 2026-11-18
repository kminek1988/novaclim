from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django import forms


# Create your models here.
class About_home(models.Model):
    img1 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='img na stronę główną')
    img2 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='ikona 1')
    text1 = models.CharField(max_length=250, null=True, blank=True, verbose_name='tekst do ikony 1')
    img3 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='ikona 2')
    text2 = models.CharField(max_length=250, null=True, blank=True, verbose_name='tekst do ikony 2')
    img4 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='ikona 3')
    text3 = models.CharField(max_length=250, null=True, blank=True, verbose_name='tekst do ikony 3')

    img5 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='ikona 5')
    text4 = models.CharField(max_length=250, null=True, blank=True, verbose_name='tekst do ikony 4')


    content = RichTextField(null=True, blank=True, verbose_name="tekst na sekcję")




    
    

    class Meta:
        """Meta definition for intro."""

        verbose_name = 'O mnie na stronę główną'
        verbose_name_plural = 'O mnie na stronę główną'

    def __str__(self):
         return f'zakładka O mnie na stronie głównej'



    def clean(self):
            if not self.pk and About_home.objects.exists():
                raise forms.ValidationError('Nie można utworzyć więcej niż jednej instancji modelu.')
            return super().clean()


class About(models.Model):
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'słowa klucze')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'opis dla google')
    text1 = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'Tekst na intro w zakładce')

    title = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'tytuł zakładki')
    img_bg = models.ImageField(upload_to='services/', null=True, blank=False, verbose_name='zdjęcie na tło')


    img1 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='600x401')
    img2 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='337x450')
    img3 = models.ImageField(upload_to='intro/', null=True, blank=True, verbose_name='600x401')
    content = RichTextField(null=True, blank=True, verbose_name="tekst na sekcję")
    slug = models.SlugField(null=True, blank=False, verbose_name = 'adres url')





    
    

    class Meta:
        """Meta definition for intro."""

        verbose_name = 'O mnie zakładka'
        verbose_name_plural = 'O mnie zakładka'

    def __str__(self):
         return f'zakładka O mnie'

    def get_absolute_url(self):
        return reverse('about', args=[str(self.slug)])



    def clean(self):
            if not self.pk and About.objects.exists():
                raise forms.ValidationError('Nie można utworzyć więcej niż jednej instancji modelu.')
            return super().clean()




class Paragraph(models.Model):
    about = models.ManyToManyField(About, blank=False, verbose_name='punkt w ofercie')
    content = RichTextField(null=True, blank=True, verbose_name='treść paragrafu')
    p_img = models.ImageField(upload_to='services', null=True, blank=True, verbose_name='zdjęcie do paragrafu')


    class Meta:
        verbose_name = 'Paragraf'
        verbose_name_plural = 'Paragrafy'

    def __str__(self):
        service_str = str(self.service)
    
    # Pobierz pierwsze 10 słów z content
        content_words = self.content.split()[:10]  
        content_str = ' '.join(content_words)  
    
    # Zwróć połączony string
        return f"{service_str} - {content_str}"