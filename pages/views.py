from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, price_choices, state_choices

from listings.models import Listing
from brokers.models import Broker


def index(request):
    # gather all ojects in listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # pagination
    # max objevt per page
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    # define a key pair var
    context={
        'listings'        : paged_listing,
        'bedroom_choices' : bedroom_choices,
        'price_choices'   : price_choices,
        'state_choices'   : state_choices


    }

    #connected to the template index.html
    return render(request, 'pages/index.html', context)

  
def about(request):
    #connected to the template about.html
    brokers = Broker.objects.order_by('-hire_date')

    #get MVP
    mvp_brokers = Broker.objects.all().filter(is_mvp=True)

    contex = {
        'brokers':brokers,
        'mvp_brokers':mvp_brokers,
    }

    #return
    return render(request, 'pages/about.html', contex)