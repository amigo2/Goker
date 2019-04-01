# Listing view
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
 
from .models import Listing


# indek view
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
        'state_choices'   : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices'   : price_choices,
    }
    # return and render listing.html
    return render(request, 'listings/listings.html', context)

# listing view
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
 
    context = { 
        'listing':listing

    }
    return render(request, 'listings/listing.html', context)

# search view
def search(request):

    query_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains = keywords)

    context = {
        'state_choices'   : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices'   : price_choices,
        'listings'        : query_list
    }
    return render(request, 'listings/search.html', context)
    