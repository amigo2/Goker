# Listing view
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
 
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
        'listings' : paged_listing

    }
    # return and render listing.html
    return render(request, 'listings/listings.html', context)

# linsting view
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
 
    context = { 
        'listing':listing

    }
    return render(request, 'listings/listing.html', context)

# search view
def search(request):
    return render(request, 'listings/search.html')