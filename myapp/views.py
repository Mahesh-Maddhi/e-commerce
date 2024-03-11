from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from myapp.models import Contact
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
    context = {}
    if request.method == "GET":
        
        query = request.GET.get("q")
        url = "https://dummyjson.com/products/search?q=" + str(query)
        products = get_data(url)
        products = products["products"]
        if len(products) > 0:
            context = {"products":products}
            
    print(context)
   
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

    context = None
    if request.method == "GET" and len(request.GET)>0: 
        form_type = request.GET.get('form')
        print(request.GET)
        # category form
        if form_type == "category":
            category = request.GET.get('category')
            url = 'https://dummyjson.com/products/category/'+ str(category)
            products = get_data(url)
            context = {"products":products['products']}

        elif form_type == "product":
            # form from product-card
            product_id = request.GET.get('product_id')
            
            product_details_data = {"product_id":product_id}
            
            #sending session data to product-details
            request.session['product_details_data'] = product_details_data
            return redirect('/product-details')
    else:

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
            user_message = request.POST.get("user_message")
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

    products = get_data('https://dummyjson.com/products?limit=3')
    context = {"products":products["products"]}
    return render(request, 'cart.html',context)