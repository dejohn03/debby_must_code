def add_to_cart(item,cart=[]):
    if cart is None:
        cart = []

        cart.append(item)
    return cart

    cart1 = add_to_cart("laptop")
    print(cart1)
    cart2 = add_to_cart("mouse")
    print(cart2)
    