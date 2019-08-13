from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

import json
from django.core import serializers

from calendar_api.models import Events
from listings.models import Listing

# Create your views here.


def index(request):

    events = Events.objects.order_by('-date_created')

    context = {
        'events': events,
    }

    return render(request, 'calendar/calendar.html', context )


'''def index(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_name')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        if request.GET.get('title') == "all":
            all_events = Events.objects.all()
        else:   
            all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_name'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")

            event_sub_arr['start_date'] = start_date
            event_sub_arr['end_date'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request,'calendar/calendar.html',context)'''