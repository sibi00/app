from django.shortcuts import render_to_response
from django.template import RequestContext
from strona.models import Country,Countrylanguage
# Create your views here.
from django.db import connection
import json
import collections

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def index(request):
    return render_to_response('index.html')

def countries(request):
    cursor = connection.cursor()
    cursor.execute("Select * from  Country join Countrylanguage on Country.code = Countrylanguage.countrycode order by Country.continent asc, Country.name asc, Countrylanguage.percentage desc;")
    row = dictfetchall(cursor)
    connection.close()
    return render_to_response('countries.html',{'kraje':row})

def groupedCountries(request):
    return render_to_response('groupedCountries.html')

def countrycode(request,kraj):
    cursor = connection.cursor()
    cursor.execute("Select * from  Countrylanguage where countrycode='%s';" % kraj[:3])
    row1 = dictfetchall(cursor)

    #row = Countrylanguage.objects.raw("Select countrycode, percentage from  Countrylanguage where countrycode='%s';" % kraj[:3])
    j = json.dumps(row1)
    objects_file = "./country/%s.json" % (kraj[:3])
    f = open(objects_file,'w')
    print >> f, j
    f.close();
    connection.close()
    return render_to_response('countrycode.html',{'kraje':row1})