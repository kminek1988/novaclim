from django.contrib import admin
from .models import (Paragraph,
                     Service,
                     Download)
# Register your models here.
admin.site.register(Paragraph)
admin.site.register(Service)
admin.site.register(Download)