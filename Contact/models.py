from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
# Create your models here.
class Social(models.Model):
    name = models.CharField(max_length = 150, null=True, blank=True, verbose_name='media społecznościowe')
    url = models.URLField(null=True, blank=True, verbose_name='adres url do konta')
    icon = models.ImageField(upload_to='socials/', null=True, blank=True, verbose_name='ikonka platformy/logo')
    
    
    

    # TODO: Define fields here

    class Meta:

        verbose_name = 'Medium społecznościowe'
        verbose_name_plural = 'Media społecznościowe'

    def __str__(self):
        return self.name



class ContactData(models.Model):
    

    name = models.CharField("Nazwa", max_length=255, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    phone_number = models.CharField(verbose_name= "Numer telefonu", max_length=15, blank=True, null=True)
    phone_number2 = models.CharField(verbose_name="Numer telefonu bez żadnych znaków", max_length=15, blank=True, null=True)

    street = models.CharField(verbose_name="Ulica", max_length=100, blank=True, null=True)
    nr = models.IntegerField(null=True, blank=True)
    
    city = models.CharField(verbose_name="Miasto", max_length=100, blank=True, null=True)
    postal_code = models.CharField(verbose_name="Kod pocztowy", max_length=10, blank=True, null=True)
    logo = models.ImageField("Logo", upload_to='logos/', blank=True, null=True)
    socials = models.ManyToManyField(Social, verbose_name='media społecznościowe', blank=True, null=True)
    tax = models.CharField("NIP", max_length=10, blank=True, null=True)

    
    class Meta:
        verbose_name = "Dane kontaktowe"
        verbose_name_plural = "Dane kontaktowe"
    def __str__(self):
        return f'Dane kontaktowe'
    def save(self, *args, **kwargs):
        if ContactData.objects.exists() and not self.pk:
            raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
        return super(ContactData, self).save(*args, **kwargs)
    


class Private(models.Model):
    polityka =RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name='data utworzenia')

    
    class Meta:
        
        verbose_name = 'Polityka prywatności'
        verbose_name_plural = 'Polityka prywatności'

    def __str__(self):
        return str(self.date)
    def save(self, *args, **kwargs):
            if Private.objects.exists() and not self.pk:
                raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
            return super(Private, self).save(*args, **kwargs)
    



class Impressum(models.Model):
    impressum = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name='data utworzenia')

    
    class Meta:
        
        verbose_name = 'Impressum'
        verbose_name_plural = 'Impressum'

    def __str__(self):
        return str(self.date)
    

    def save(self, *args, **kwargs):
            if Impressum.objects.exists() and not self.pk:
                raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
            return super(Impressum, self).save(*args, **kwargs)
    


class Agb(models.Model):
    content = RichTextField(null=True, blank=True, verbose_name='treść')
    date = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name='data utworzenia')

    
    class Meta:
        
        verbose_name = 'RODO'
        verbose_name_plural = 'RODO'

    def __str__(self):
        return str(self.date)
    def save(self, *args, **kwargs):
            if Agb.objects.exists() and not self.pk:
                raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
            return super(Agb, self).save(*args, **kwargs)



class Logo(models.Model):
    img = models.ImageField(upload_to='logo/',null=True, blank=True, verbose_name="plik graficzny")
    fav = models.ImageField(upload_to='logo/',null=True, blank=True, verbose_name="plik favicon 16x16")
    fav2 = models.ImageField(upload_to='logo/',null=True, blank=True, verbose_name="plik favicon 32x32")



    # TODO: Define fields here

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'

    def __str__(self):
        return f'logo'
    def save(self, *args, **kwargs):
            if Logo.objects.exists() and not self.pk:
                raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
            return super(Logo, self).save(*args, **kwargs)






class ContactForm(models.Model):
    email = models.EmailField(null=True, blank=False)
    name = models.CharField(
        max_length=255, verbose_name='imię', blank=True, null=True)
    surname = models.CharField(
        max_length=255, verbose_name='nazwisko', blank=True, null=True)
    tel = models.CharField(null=True, blank=True, max_length=100,
                              verbose_name='numer telefonu')
    temat = models.CharField(null=True, blank=True, max_length=100,
                              verbose_name='temat')
    content = models.TextField(
        blank=False, null=True, verbose_name='treść wiadomości')
    policy = models.BooleanField(
        blank=False, null=True, verbose_name='Akceptuję zasady polityki prywatności')

    class Meta:
        verbose_name = 'Wiadomość z formularza kontaktowego'
        verbose_name_plural = 'Wiadomości z formularza kontaktowego'

    def __str__(self):
        return f'{self.email}-----> {self.temat}'

class ContactFormThanks(models.Model):
    content = RichTextField(null=True, blank=True, verbose_name='podzdiękowanie za przesłanie formularza kontaktowego')
    class Meta:
        verbose_name = 'podzdiękowanie za przesłanie formularza kontaktowego'
        verbose_name_plural = 'podzdiękowanie za przesłanie formularza kontaktowego'

    def __str__(self):
        return f'podzdiękowanie za przesłanie formularza kontaktowego'
    def save(self, *args, **kwargs):
            if ContactFormThanks.objects.exists() and not self.pk:
                raise ValidationError('Można dodać tylko jeden model. Jeżeli chcesz coś zmienić, wejdź w model i zmień jego pola. W innym wypadku skontaktuj się z programistą')
            return super(ContactFormThanks, self).save(*args, **kwargs)
