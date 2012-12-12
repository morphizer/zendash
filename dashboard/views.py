from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import simplejson

from dashboard.lib.ZenossAPI import ZenossAPI
from dashboard.models import Configuration
from dashboard.forms import ConfigurationForm

def index(request):
    try:
        config = Configuration.objects.get(pk=1)
        refresh_interval = config.refresh_interval
        return render(request, 'home.html', {
            'refresh_interval': refresh_interval, 
        })

    except Configuration.DoesNotExist:
        return render(request, 'home.html')

def getevents(request):
    config = Configuration.objects.get(pk=1)
    z = ZenossAPI( config.zenoss_instance, 
                   config.zenoss_username,
                   config.zenoss_password
                 )
    events = z.get_events(showAck = config.show_acknowledged)

    return HttpResponse(simplejson.dumps(events))

def configuration(request):
    if request.method == 'POST':
        try:
            config = Configuration.objects.get(pk=1)
            form = ConfigurationForm(request.POST, instance=config)
        except Configuration.DoesNotExist:
            form = ConfigurationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        try:
            config = Configuration.objects.get(pk=1)
            # Radio button doesn't seem to be properly filled in, so add it manually
            form = ConfigurationForm(instance=config, initial={'show_acknowledged': config.show_acknowledged})
        except Configuration.DoesNotExist:
            form = ConfigurationForm()

    return render(request, 'configuration.html', {
        'form': form,
    })
