from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_at')  # Ganti dengan field yang sesuai

admin.site.register(Contact, ContactAdmin)