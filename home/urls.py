from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Product
    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),

    # Cart
    path(
        'add-to-cart/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'remove/<int:id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'plus/<int:id>/',
        views.increase_quantity,
        name='plus'
    ),

    path(
        'minus/<int:id>/',
        views.decrease_quantity,
        name='minus'
    ),

    # Checkout & Orders
    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'orders/',
        views.orders,
        name='orders'
    ),

    # Contact
    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    # Wishlist
    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'
    ),

    path(
        'wishlist/add/<int:id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),

    path(
        'wishlist/remove/<int:id>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),

    # Login System
    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'login/',
        views.login_user,
        name='login'
    ),

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),
]