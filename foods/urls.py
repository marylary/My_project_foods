from django.urls import path

from foods.views import *

urlpatterns = [
    path('', register, name = 'register'),
    path('login', connect, name = 'login'),
    path('home', home, name = 'home'),
    path('shop', shop, name = 'shop'),
    path('about', about, name = 'about'),
    path('blog', blog, name = 'blog'),
    path('blogsingle', blogsingle, name = 'blogsingle'),
    path('contact', contact, name = 'contact'),
    path('cart', cart, name = 'cart'),
    path('checkout', checkout, name = 'checkout'),
    path('wishlist', wishlist, name = 'wishlist'),
    path('product', product, name = 'product'),
    path('single', single, name = 'single')
]



