from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from myapp.models import SignedUser, Contact
import requests


# Create your views here.

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error occured while api fetch with status code":response.status_code}
    

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
    if request.method == "POST":
        # product form
        if request.POST.get('form') == "product":
            product_id = request.POST.get('product_id')
            product_details_data = {"product_id":product_id}
            #sending session data to product-details
            request.session['product_details_data'] = product_details_data
            return redirect('/product-details')
            # search form
        elif request.POST.get("form") == "search":
            query = request.POST.get("query")
            # sending session data to search
            request.session['query'] = query
            return redirect("/search")
    context = {}
        # from Home page categories
    if request.session.get('products') is not None:
        products = request.session.get('products')
        context = {"products":products}
        request.session['products'] = None
    else:
        # for searching
        query = request.session.get('query',{})
        url = "https://dummyjson.com/products/search?q=" + str(query)
        products = get_data(url)
        context = {"products":products['products']}
        request.session['query'] = None
    print("SEARCHED")
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
            messages.error(request,"Please enter same password as above!")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already in use try another one!")
            else:
                try:
                    user = User.objects.create_user(username = username,email = email, password = password)
                except Exception as e:
                    messages.error(request,f"Something went wrong: {e}")

                user.save()
                messages.success(request,"Registered Successfully!")
                return redirect("/login")
    return render(request,'signup.html')
    
        
def user_logout(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect('/login')


def home(request):
    if request.method == "POST":
        if request.POST.get("form") == "search":
            query = request.POST.get("query")
            # sending session data to search
            request.session['query'] = query
            return redirect("/search")
        else:
            category = request.POST.get('category')
            url = 'https://dummyjson.com/products/category/'+ str(category)
            products = get_data(url)
            # sending session data to shop
            request.session['products'] = products["products"]
            return redirect('/search')
    
    products = get_data('https://dummyjson.com/products')
    categories = get_categories(products)
    
    
    context={
        "username":request.user.username,
        "products":products["products"],
       "categories":categories
    }
    
    return render(request,'index.html',context)
    
    

def about(request):
    if request.POST.get("form") == "search":
            query = request.POST.get("query")
            # sending session data to search
            request.session['query'] = query
            return redirect("/search")
    
    return render(request,'about.html')
    return redirect('/login')
    

def shop(request):
    
    if request.method == "POST":
            # search form
        if request.POST.get("form") == "search":
            query = request.POST.get("query")
            # sending session data to search view
            request.session['query'] = query
            return redirect("/search")
        else:
            # form from product-card
            product_id = request.POST.get('product_id')
            
            product_details_data = {"product_id":product_id}
            
            #sending session data to product-details
            request.session['product_details_data'] = product_details_data
            return redirect('/product-details')
    
    products = get_data('https://dummyjson.com/products')

    context = {
        "products":products['products']
    }

    
    return render(request,'display_products.html',context)
    

def contact(request):
    
    # user contact form
    if request.method == "POST":
            #search form
        if request.POST.get("form") == "search":
            query = request.POST.get("query")
            # sending session data to search
            request.session['query'] = query
            return redirect("/search")
            # contact form
        elif request.POST.get("form") == "contact":
            first_name = request.POST.get("firstname")
            last_name = request.POST.get("lastname")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            user = authenticate(email=email)

            if user is not None:
                try:
                    contact = Contact(firstname=first_name,lastname = last_name,phone = phone, email = email)
                    contact.save()
                    messages.success(request,"Your details Submitted Succesfully.")
                except Exception as error:
                    messages.warning(request, error)

            else:
                messages.error(request, " User details already exist!")

    return render(request,'contact.html',{"username":request.user.username})

    
def product_details(request):
    if request.method == "POST":
        if request.POST.get("form") == "search":
                query = request.POST.get("query")
                # sending session data to search
                request.session['query'] = query
                return redirect("/search")

    product_details = request.session.get('product_details_data',{})
    
    product_id = product_details['product_id']
    if product_id == None:
        product_id = 1
    url = 'https://dummyjson.com/products/'+ str(product_id)

    product = get_data(url)
    
    context = {"product" : product}

    return render(request,'productDetails.html',context)

@login_required
def cart(request):
    products = get_data('https://dummyjson.com/products?limit=3')
    context = {"products":products["products"]}
    return render(request, 'cart.html',context)