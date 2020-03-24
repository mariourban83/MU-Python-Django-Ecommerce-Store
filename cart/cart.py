from django.conf import settings
from decimal import Decimal
from shop.models import Product


class Cart(object):
    """
    Create and initialize empty cart
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        """
        Create and save an empty card dictionary to the session if card
        is not present.
        """
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    """
    Method for adding item(s) to the card or to update quantity.
    Product ID used as a key in the cart's content dictionary.
    To serialize session data, product ID and price are converted into string
    """
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    """
    Method for removing item(s) from the card.
    """
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    """
    For iterating over the items in the cart
    and retrieve products from db
    """
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.object.filter(id_in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    """
    Custom method for returning total number of items
    currently in cart.
    """
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    """
    Method for calculating total cost of item in cart
    """
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    """
    Method for clearing the cart session
    """
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
