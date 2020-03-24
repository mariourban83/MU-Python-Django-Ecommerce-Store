from .cart import Cart


def cart(request):
    """
    Function that returns dict of objects as a variable named cart
    available to all templates rendered using RequestContext.
    """
    return {'cart': Cart(request)}
