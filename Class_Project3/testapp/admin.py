from django.contrib import admin
from testapp.models import company
# Register your models here.

class companyadmin(admin.ModelAdmin):
    list_display = ['name','ceo','city']

admin.site.register(company,companyadmin)
