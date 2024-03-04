from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
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
        print("hello")
        category = request.POST.get('category')
        print(category)
    
    products = get_data('https://dummyjson.com/products')
    categories = get_categories(products)
    
    
    context={
        "username":request.user.username,
        "products":products["products"],
       "categories":categories
    }
    
    if request.user.is_authenticated:
        return render(request,'index.html',context)
    
    return redirect('/login')
    

def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html',{"username":request.user.username})
    return redirect('/login')
    

def shop(request):
    # product form
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        
        product_details_data = {"product_id":product_id}
        
        #sending session data to product-details
        request.session['product_details_data'] = product_details_data
        return redirect('/product-details')
    
    products = get_data('https://dummyjson.com/products')

    context = {
        "products":products['products']
    }
    if request.user.is_authenticated:
        return render(request,'shop.html',context)
    return redirect('/login')
    

def contact(request):
    
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        user = authenticate(phone=phone)
        if user is not None:
            try:
                contact = Contact(firstname=first_name,lastname = last_name,phone = phone, email = email)
                contact.save()
                messages.success(request,"Your details Submitted Succesfully.")
            except Exception as error:
                messages.warning(request, error)

        else:
            messages.error(request, " User details already exist!")

    if request.user.is_authenticated:
        return render(request,'contact.html',{"username":request.user.username})

    return redirect('/login')
    
def product_details(request):

    product_details = request.session.get('product_details_data',{})
    print(product_details)
    product_id = product_details['product_id']
    url = 'https://dummyjson.com/products/'+ str(product_id)
    product = get_data(url)
    print(product)


    context = {"product" : product}

    if request.user.is_authenticated:
        return render(request,'productDetails.html',context)
    return redirect('/login')