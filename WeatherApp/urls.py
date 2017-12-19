from django.conf.urls import patterns, include, url
from app.models import *
from app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getdata/$', getdata),
    url(r'^getDataForChart/$', getDataForChart),
    url(r'^renderCharts/$', renderCharts),
    url(r'^getAllRegions/$', getAllRegions),
    url(r'^getAllYears/$', getAllYears),
    url(r'^getAllTempTypes/$', getAllTempTypes),
)
