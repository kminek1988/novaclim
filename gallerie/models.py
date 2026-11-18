from django.db import models
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Tytuł zdjęcia')    
    date = models.DateField(null=True, blank=True, verbose_name='data dodania lub imprezy')
    description = models.CharField(null=True, blank=True, verbose_name="opis zdjęcia", max_length=300)
    slug = models.SlugField(null=True, blank=False, verbose_name='nazwa wyświetla się w kodzie- Ważne dla pozycjonowania')
    img = models.ImageField(null=True, blank=True, verbose_name='zdjęcie', upload_to='galeria')
    class Meta:
        
        
        verbose_name = 'zdjęcie do galerii'
        verbose_name_plural = 'zdjęcia do galerii'

    def __str__(self):
        return self.title
    
    


