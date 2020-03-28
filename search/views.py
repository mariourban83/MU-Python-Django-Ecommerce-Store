from django.shortcuts import render
from shop.models import Product
from django.db.models import Q


def search(request):
    title = "LR Ireland | Search Results"
    query = request.GET.get('q')
    result = Product.objects.filter(
             Q(name__icontains=query) | Q(description__icontains=query)
             )
    return render(request, 'search/search.html',
                  {'result': result,
                   'title': title})
