from django.shortcuts import render, get_object_or_404
from .models import Category, Product

"""
Product Catalog view to display all available products
or to display products filtered by category.
"""


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'products': products,
                   'category': category,
                   'categories': categories})


"""
Single Product view to display product detail page via ID.
Slug passed in for urls building
"""


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html',
                  {'product': product})
