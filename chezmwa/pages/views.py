from django.shortcuts import render, get_object_or_404
from .models import Listing, Neighborhood
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')
    neighborhoods = Neighborhood.objects.all()

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'neighborhoods': neighborhoods,
    }


    return render(request, 'pages/index.html', context)

def listing(request, pk):
    listing = Listing.objects.get(id=pk)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def listings(request):
    #neighborhoods = Neighborhood.objects.all()
    listings = Listing.objects.order_by('-list_date')
    neighborhood_list = request.GET.get('neighborhood_list')

    if neighborhood_list != '' and neighborhood_list is not None:
        listings = listings.filter(neighborhood__neighborhood_name__exact=neighborhood_list)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


# This function is to be used in the search function
# It's to make the query condition not to be repetitive
def is_valid_query_param(param):
    return param != '' and param is not None

def search(request):
    listings = Listing.objects.order_by('-list_date')
    neighborhood_query = request.GET.get('neighborhood')
    price_query = request.GET.get('price')
    bedroom_query = request.GET.get('bedroom')
    bathroom_query = request.GET.get('bathroom')

    if is_valid_query_param(neighborhood_query) and neighborhood_query != 'Select Neigborhood':
        listings = listings.filter(neighborhood__neighborhood_name=neighborhood_query)

    if is_valid_query_param(price_query) and price_query != 'Select price in CFA':
        listings = listings.filter(price__lte=price_query)

    if is_valid_query_param(bedroom_query) and bedroom_query != 'Select Number of Bedrooms':
        listings = listings.filter(bedrooms=bedroom_query)

    if is_valid_query_param(bathroom_query) and bathroom_query != 'Select Number of Bathrooms' :
        listings = listings.filter(bathrooms=bathroom_query)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/search.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        message = request.POST['message']
        

    return render(request, 'listings/contacts.html')
