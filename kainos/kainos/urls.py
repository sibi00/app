from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kainos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','strona.views.index'),
    url(r'^countries/$','strona.views.countries'),
    url(r'^groupedCountries/$','strona.views.groupedCountries'),
    url(r'^country/(?P<kraj>([A-Z]{3})/$)','strona.views.countrycode'),
]
