from django.urls import reverse
# tylko jeden model 
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.serializers import serialize

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views import View
from .models import (
    Intro,
)
from About.models import (
    About_home,
    About,
)

from Contact.models import (
    Private,
    Impressum,
    Agb,
    ContactForm,
    ContactFormThanks
)
from gallerie.models import (
    Image,
)
from Contact.forms import PostForm
from Services.models import Service, Paragraph
from django.http import JsonResponse
from django.core.serializers import serialize
class Homepl(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        intro = Intro.objects.first()
        about = About_home.objects.first()
        services = Service.objects.all()
        about_section = About.objects.first()
        context['intro'] = intro
        context['about'] = about
        context['services'] = services
        context['about_section'] = about_section
        
        return context

    
class AboutView(DetailView):
    model = About
    template_name = 'about.html'

class ServiceView(DetailView):
    model = Service
    template_name = 'service.html'


class ContactView(TemplateView):
    template_name = 'contact-section.html'
    
    

class RequestContact(TemplateView):
    template_name = 'contact.html'
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            if form.is_valid():
                instance = form.save(commit=False)

                instance.save()
                print(instance)

            
                

                # Wysyłanie wiadomości e-mail
                subject = "Nowa wiadomość z formularza"
                content = form.cleaned_data['content']  # Zakładam, że masz pole 'content' w formularzu
                from_email = settings.EMAIL_HOST_USER
                to_email = [settings.EMAIL_HOST_USER]

                send_mail(subject, content, from_email, to_email)
                
                message = ContactFormThanks.objects.first()
     
                serialized_obj = serialize('json', [message, ])
                print(serialized_obj)
                
                return JsonResponse({
                        'message_content': message.content
                          })
                          

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["form"] = PostForm()
            return context
            


class PrivateView(TemplateView):
    template_name = 'private.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = Private.objects.first()
        return context
    




class ImpressumView(TemplateView):
    template_name = "impressum.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = Impressum.objects.first()
        return context



class agbView(TemplateView):
    template_name = "agb.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = Agb.objects.first()
        return context


class GallerieListView(ListView):
    model = Image
    template_name = 'gallerie.html'



# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'

# class BookCreateView(CreateView):
#     model = Book
#     template_name = 'book_form.html'
#     fields = ['title', 'author', 'published_date']

# class BookUpdateView(UpdateView):
#     model = Book
#     template_name = 'book_form.html'
#     fields = ['title', 'author', 'published_date']

# class BookDeleteView(DeleteView):
#     model = Book
#     template_name = 'book_confirm_delete.html'
#     success_url = reverse_lazy('book_list')
