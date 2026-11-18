from Contact.models import ContactData, Social, Logo
from Services.models import Service
from About.models import About, About_home
from Homepage.views import RequestContact

def contact_data(request):
    try:
        contact_data = ContactData.objects.first()
    except ContactData.DoesNotExist:
        contact_data = None

    return {'contact_data': contact_data}


def service_data(request):
    service_data = Service.objects.all()
    return {'service_data': service_data}


def about_data(request):
    about_data = About.objects.first()
    about_home = About_home.objects.first()
    context = {
        'about_home': about_home,
        'about_data': about_data
    }
    return context





def social_data(request):
    social = Social.objects.all()
    return {'social': social}



def logo_data(request):
    logo = Logo.objects.first()
    return {'logo': logo}


def contactform(request):
    view = RequestContact()
    context = view.get_context_data()
    return context