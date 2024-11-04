from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Task)


from django.contrib import admin
from .models import ContactDetail

@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_no', 'address')
    search_fields = ('name', 'email', 'mobile_no')









