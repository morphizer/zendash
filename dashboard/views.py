from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import simplejson

from dashboard.lib.ZenossAPI import ZenossAPI
from dashboard.models import Configuration
from dashboard.forms import ConfigurationForm

def index(request):

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
        config = Configuration.objects.get(pk=1)
        form = ConfigurationForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        try:
            config = Configuration.objects.get(pk=1)
            form = ConfigurationForm(instance=config)
        except Configuration.DoesNotExist:
            form = ConfigurationForm()

    return render(request, 'configuration.html', {
        'form': form,
    })

