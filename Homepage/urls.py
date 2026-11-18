from django.urls import path, include
from .views import (Homepl,
                    AboutView,
                    ServiceView,
                    ContactView,
                    PrivateView,
                    ImpressumView, 
                    agbView,
                    GallerieListView,
                    RequestContact)


urlpatterns = [
    path('', Homepl.as_view(), name='home'),
    path('1/<str:slug>/', AboutView.as_view(), name='about'),
    path('angebot/<str:slug>/', ServiceView.as_view(), name='services'),
    path('kontakt/', ContactView.as_view(), name='contact'),
    path('daten/', PrivateView.as_view(), name='polityka'),
    path('impressum/', ImpressumView.as_view(), name='impressum'),
    path('agb/', agbView.as_view(), name='agb'),
    path('photos/', GallerieListView.as_view(), name='gallerie'),
    path('contactform/', RequestContact.as_view(), name='contact-form'),



]
