from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    title = "LR Ireland | Home"
    products = Product.objects.all
    return render(request, 'shop/home.html', {'products': products,
                                              'title': title})


def contact(request):
    title = "LR Ireland | Contact"
    return render(request, 'shop/contact.html', {'title': title})


def faq(request):
    title = "LR Ireland | FAQ"
    return render(request, 'shop/faq.html', {'title': title})


"""
Product Catalog view to display all available products
or to display products filtered by category.
"""


def product_list(request, category_slug=None):
    title = "LR Ireland | All Products"
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'products': products,
                   'category': category,
                   'categories': categories,
                   'title': title})


"""
Single Product view to display product detail page via ID.
Slug passed in for urls building
"""


def product_detail(request, id, slug):
    title = "LR Ireland | Product Detail"
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'title': title})


def special_offers(request):
    title = "LR Ireland | Special Offers"
    products = Product.objects.filter(special_offer=True)
    return render(request, 'shop/special_offers.html', {'products': products,
                                                        'title': title})
