from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import Weather
from app.serializer import *
import requests
import csv
import re
import json


def getdata(request):
    regions = ['UK']
    Ttypes = ['Tmin']
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    try:
        for region in regions:
            for Ttype in Ttypes:
                url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"+Ttype+"/date/"+region+".txt"
                rData = requests.get(url)
                textdata = rData.content
                blankLineIndex = textdata.find('\r\n\r\n')
                data = textdata[blankLineIndex + 1:]
                data = re.sub(' +', ' ', data).strip()
                reader = csv.DictReader(data.splitlines(), delimiter=' ')
                for record in reader:
                    year = record.pop('Year', None)
                    for month in record:
                        print month
                        if month in months:
                            weatherObj = Weather()
                            weatherObj.year = int(year)
                            weatherObj.month = month
                            weatherObj.data = float(record[month])
                            weatherObj.region = region
                            weatherObj.Ttype = Ttype
                            weatherObj.save()
        return HttpResponse('Data Saved Successfully....')
    except:
        return HttpResponse('Server Error....')


def getDataForChart(request):
    region = request.GET.get('region')
    type = request.GET.get('type')
    year = int(request.GET.get('year'))
    weatherObjs = Weather.objects.filter(region=region, Ttype=type, year=year)
    if len(weatherObjs) > 0:
        return HttpResponse(json.dumps(minWeatherSerializer(weatherObjs, many=True).data), content_type="application/json")
    else:
        return HttpResponse(0)


def getAllRegions(request):
    weatherObjs = Weather.objects.all().values_list('region', flat=True).distinct()
    if len(weatherObjs) > 0:
        return JSONResponse(weatherObjs)
    else:
        return HttpResponse(0)

def getAllYears(request):
    weatherObjs = Weather.objects.all().values_list('year', flat=True).distinct()
    if len(weatherObjs) > 0:
        return JSONResponse(weatherObjs)
    else:
        return HttpResponse(0)

def getAllTempTypes(request):
    weatherObjs = Weather.objects.all().values_list('Ttype', flat=True).distinct()
    if len(weatherObjs) > 0:
        return JSONResponse(weatherObjs)
    else:
        return HttpResponse(0)

def renderCharts(request):
    return render_to_response('renderCharts.html', context_instance=RequestContext(request))