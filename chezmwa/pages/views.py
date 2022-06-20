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


def about(request):
    return render(request, 'pages/about.html')

def faqs(request):
    return render(request, 'pages/faqs.html')
