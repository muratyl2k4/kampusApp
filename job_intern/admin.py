from django.contrib import admin
from .models import InternPlace , InternAnnouncement , InternCategory

admin.site.register(InternPlace)
admin.site.register(InternCategory)
admin.site.register(InternAnnouncement)

# Register your models here.
