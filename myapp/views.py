from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from myapp.models import Contact, Cart
from django.conf import settings
import requests


# Create your views here.

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()
    else:
        return { "message" :f"error occured while api fetch with status code:{response.status_code}"}
    
def add_total_price(items_queryset):
    items_list = list(items_queryset)

    total_cost = 0
    for item in items_list:
        item.total_price = int(item.price) * item.quantity
        total_cost += int(item.price) * item.quantity
    return {"products":items_list,"total_cost":total_cost}


def get_categories(api_response):

    categories = []
    for product in api_response["products"]:
        category = product["category"]
        thumbnail_image = product["thumbnail"]

        category_exists = any(d["name"] == category for d in categories)
        if not category_exists:
            categories.append({"name": category, "image": thumbnail_image})
    

    return categories


def search(request):
    context = {}
    if request.method == "GET":
        query = request.GET.get("q")
        url = "https://dummyjson.com/products/search?q=" + str(query)
        products = get_data(url)
        products = products["products"]
        if len(products) > 0:
            context = {"products":products}
        else:
            context = {"query":query}
   
    return render(request,"display_products.html",context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            # User validation
            user = authenticate(username = username, password = password)
            
            if user is not None:
                messages.success(request, "You Logged in Successfully.")
                login(request,user)
                return redirect("/home")
            else:
                messages.warning(request, "Please enter valid Username and Password!")
    except Exception as e:
        messages.warning(request,f"Something Went Wrong : {e}")
    
    return render(request,'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        if password != confirm_password:
            messages.error(request,"Password does not matched.")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken use another one!")
            else:
                try:
                    user = User.objects.create_user(username = username,email = email, password = password)
                    user.save()
                    messages.success(request,"Registered Successfully!")
                except Exception as e:
                    messages.error(request,f"Something went wrong: {e}")

                return redirect("/login")
    return render(request,'signup.html')
    
        
def user_logout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect('/home')


def home(request):
    
    products = get_data('https://dummyjson.com/products')
    categories = get_categories(products)
    context={
        "username":request.user.username,
        "products":products["products"],
       "categories":categories
    }
    
    return render(request,'index.html',context)
    
    

def about(request):

    return render(request,'about.html')
    

def shop(request):
        # For Specific Categoy
    if request.GET.get('category') != None: 
        category = request.GET.get('category')
        url = 'https://dummyjson.com/products/category/'+ str(category)
        products = get_data(url)
        context = {"products":products['products']}
    else:
        # For all products
        products = get_data('https://dummyjson.com/products')
        context = {
            "products":products['products']
        }

    return render(request,'display_products.html',context)
    

def contact(request):
    
    # user contact form
    if request.method == "POST":
        if request.POST.get("form") == "contact":
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            user_message = request.POST.get("message")
            user_exist = Contact.objects.filter(email=email).exists()

            if not user_exist:
                try:
                    contact = Contact(full_name = full_name, email = email, user_message = user_message)
                    contact.save()
                    messages.success(request,"Your details Submitted Succesfully.")
                except Exception as error:
                    messages.warning(request, error)

            else:
                messages.warning(request, "User details already exist!")
    return render(request,'contact.html')

    
def product_details(request):
    product_id = 1
    if request.method == "GET":
        product_id = request.GET.get('product_id')

    url = 'https://dummyjson.com/products/'+ str(product_id)
    product = get_data(url)
    context = {"product" : product}
    return render(request,'productDetails.html',context)

@login_required
def cart(request):
    if request.method == "POST":
        form_type = request.POST.get('form')
        if form_type == 'buy':
            id = request.POST.get('product-id')
            return redirect(f'/purchase?product_id={id}')
        elif form_type == 'delete':
             id = request.POST.get('product-id')
             if Cart.objects.filter(product_id = id).exists():
                cart_product = Cart.objects.get(product_id = id)
                cart_product.delete()
            # to update quantity
        elif form_type == 'update':
            id = request.POST.get('product-id')
            updated_quantity = request.POST.get('quantity')
            updated_quantity = int(updated_quantity)

            if Cart.objects.filter(product_id = id).exists():
                cart_product = Cart.objects.get(product_id = id)
                cart_product.quantity = updated_quantity
                cart_product.save()

        elif form_type == 'add-to-cart':
            id = request.POST.get('product-id')
            
            
            if Cart.objects.filter(product_id = id).exists():
                # messages.success(request,"Item Is Already In The Cart")
                pass

            # adding items to cart
            else:
                product = get_data('https://dummyjson.com/products/'+ str(id))
                product_id = product['id']
                product_title = product['title']
                product_thumbnail = product['thumbnail']
                product_brand = product['brand']
                product_price = product['price']
                quantity = 1

                try:
                    user = User.objects.get(username=request.user)
                except User.DoesNotExist:
                    return redirect('/login')
                    
                cart_item = Cart(product_id = product_id,
                                 username = user, 
                                 title = product_title, 
                                 thumbnail = product_thumbnail,
                                 brand = product_brand,
                                 price = product_price,
                                 quantity = quantity )
                
                cart_item.save()
                messages.success(request,f"{product_title} Added to Cart Successfully! ")

    items_queryset = Cart.objects.filter(username = request.user)
    # to calculate total cost and price details 
    context = add_total_price(items_queryset)
    return render(request, 'cart.html',context)

def user_profile(request):
    return render(request,'profile.html')

@login_required
def purchase(request):
    if request.GET.get('purchase') == None:
        id = request.GET.get('product_id')
        url = 'https://dummyjson.com/products/'+ str(id)
        product = get_data(url)
        product["quantity"] = 1
        product['total_price'] = product['price']
        context = {"products":[product], "total_cost":product['total_price']}
    if request.GET.get('purchase') == "cart":
        items_queryset = Cart.objects.filter(username = request.user)
        context = add_total_price(items_queryset)
    elif request.GET.get('purchase') == "make-purchase":
        messages.success(request,"Order Placed Successfully!")
        return redirect('/shop')
    return render(request,'purchase.html',context)
    
