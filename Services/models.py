from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='nazwa oferty')
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'słowa klucze')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'opis dla google')
    text1 = models.CharField(max_length=300, null=True, blank=True, verbose_name='tekst na intro do sekcji')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name = 'tytuł zakładki')
    img_home = models.ImageField(upload_to='services/', null=True, blank=False, verbose_name='zdjęcie na stronę główną')
    img_bg = models.ImageField(upload_to='services/', null=True, blank=False, verbose_name='zdjęcie na tło')
    img_section = models.ImageField(upload_to='services/', null=True, blank=False, verbose_name='zdjęcie do sekcji')
    p_intro = RichTextField(null=True, blank=True, verbose_name='tekst na stronę główną')
    slug = models.SlugField(null=True, blank=False, verbose_name = 'adres url')

    



    

    

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Punkty do oferty'

    def __str__(self):
        return self.name
        

    def get_absolute_url(self):
        return reverse('services', args=[str(self.slug)])


class Paragraph(models.Model):
    service = models.ManyToManyField(Service, blank=False, verbose_name='punkt w ofercie')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='nazwij paragraf intuicyjnie')
    content = RichTextField(null=True, blank=True, verbose_name='treść paragrafu')
    p_img = models.ImageField(upload_to='services', null=True, blank=True, verbose_name='zdjęcie do paragrafu')


    class Meta:
        verbose_name = 'Paragraf'
        verbose_name_plural = 'Paragrafy'

    def __str__(self):
      return str(self.name)


class Download(models.Model):
    service = models.ManyToManyField(Service, null=True, blank=False, verbose_name="wybierz usługę")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='nazwa pliku do wyświetlenia na stronie')
    dokument = models.FileField(null=True, blank=True, upload_to='doc/', verbose_name='dokument do ściągnięcia')
   
    download_icon= models.ImageField(upload_to='services/', null=True, blank=True, verbose_name='ikona dokumentu')
  

    # TODO: Define fields here

    class Meta:
  

        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'

    def __str__(self):
        return self.name
