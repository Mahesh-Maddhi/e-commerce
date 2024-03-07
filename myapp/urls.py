

from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('login/', views.user_login, name="Login"),
    path('signup/', views.user_signup, name="Signup"),
    path('logout/', views.user_logout, name="logout"),
    path('home/', views.home, name="Home"),
    path('about/', views.about, name="About"),
    path('shop/', views.shop, name="Shop"),
    path('contact/', views.contact, name="Contact"),
    path('product-details/', views.product_details, name="Product-details"),
    path('search/', views.search, name="Search"),
    path('cart/', views.cart, name="Cart"),
]