from django.contrib import admin

# Register your models here.
from strona.models import *

class CountryAdmin(admin.ModelAdmin):
    list_display = ('code','name','continent','region','surfacearea','indepyear','population')

class CountrylanguageAdmin(admin.ModelAdmin):
    list_display = ('countrycode',)

admin.site.register(City)
admin.site.register(Country,CountryAdmin)
admin.site.register(Countrylanguage,CountrylanguageAdmin)
