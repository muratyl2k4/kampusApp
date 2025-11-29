from django.contrib import admin
from .models import Entry , EntryComment ,EntryLike , Topic

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(EntryComment)
admin.site.register(EntryLike)

# Register your models here.
