from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Product


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
 
 
@api_view(['GET'])
def view_cached_books(request):
    if 'product' in cache:
        # get results from cache
        print("\n\nGetting result from cache as product exists \n\n")
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)
 
    else:
        print("\n\ndb call\n\n")
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set('product', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def view_books(request): 
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)
