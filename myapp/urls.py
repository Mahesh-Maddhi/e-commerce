
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('login/', views.user_login, name="login"),
    path('signup/', views.user_signup, name="signup"),
    path('logout/', views.user_logout, name="logout"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('contact/', views.contact, name="contact"),
    path('product-details/', views.product_details, name="Product-details"),
    path('search/', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('profile/', views.user_profile, name="profile"),
    path('purchase/', views.purchase, name="purchase"),
]