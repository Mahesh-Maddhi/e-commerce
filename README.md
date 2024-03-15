# ' emart ' an e-commerce Website Project with Django

### This is a simple responsive e-commerce website project built using Django. It allows users to browse and search products, add them to cart, and proceed to checkout, create account and login.


## Features

- **User Authentication and Authorization:** Allow users to register, log in, and manage their accounts. Implement authentication and authorization to restrict access to certain parts of the site.
  
- **Product Browsing and Searching:** Users can browse through available products, through categories and search for specific items.
  
- **Shopping Cart Functionality:** Enable users to add products to their cart, view the contents of their cart, update quantities, and remove items.
  
- **Manage Profile:** Allow users to view their details in dashboard, and manage passwords or Address.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mahesh-Maddhi/e-commerce.git
    ```

2. Navigate into the project root directory:

    ```bash
    cd e-commerce
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4.  Activate the virtual environment:

    a. For bash Terminal

    ```bash
    source venv/bin/activate
    ```

    b. For windows Terminal

    ```bash
    cd venv/Scripts
    ```
    ```bash
    .\acivate
    ```
    c. navigate back to project root directory

    ```bash
    cd ../..
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Visit `http://localhost:8000` in your web browser to view the application.

## Usage

- Browse products: Navigate to the homepage to view available products in the categories or shop section.
- Register and login: Navigate to the profile to view dashboard and profile information and register/login.
- Add products to cart: Click on a product to view details, then click 'Add to Cart'.
- Proceed to checkout: Go to the cart page and click 'Make Purchase' to view order summary.
- Place order: Go to the cart page and click 'Place Order' to finalize your order.
  
## previews

- ### Home page 
<img src="static/media/images/preview/ecommerce-home-preview.png" alt="" width="800" height="500">

- ### Categories section 
<img src="static/media/images/preview/ecommerce-categories-preview.png" alt="" width="800" height="500">

- ### Shop section 
<img src="static/media/images/preview/ecommerce-shop-preview.png" alt="" width="800" height="500">

- ### Product section 
<img src="static/media/images/preview/ecommerce-product-preview.png" alt="" width="800" height="500">

- ### Cart page 
<img src="static/media/images/preview/ecommerce-cart.png" alt="" width="800" height="500">

- ### Footer page 
<img src="static/media/images/preview/ecommerce-footer-preview.png" alt="" width="800" height="500">

- ### Mobile view 
<img src="static/media/images/preview/ecommerce-mobile-preview.png" alt="" width="400" height="500">


## Responsive Design with Media Queries

To ensure your web application or website looks great on various devices,I used CSS media queries. This allowed  to apply different styles based on the characteristics of the device, such as its width.
### Design parameters
 - **Mobile View:**   device-width(425px)
 - **Tablet View:**   device-width(768px)
 - **Laptop View:**   device-width(1024px)


## Resources

- The images, logos used in this website downloaded from internet.
- The Icons used in this website embeded from [Fontawesome](https://fontawesome.com/icons).
- Some Pre coded Classes also used in this project [Bootstrap](https://getbootstrap.com/).
- Special thanks to [DummyJSON](https://dummyjson.com/) for providing product details and product images through API.


## Aknowledgement
- Thanks to [CodeWithHarry](https://www.youtube.com/@CodeWithHarry) youtube channel for providing Django Free Course.
- [Django](https://www.djangoproject.com/) documentation has been very helpful while developing the website.
- Drawing inspiration from the E-mart logo featured on [emart-Korea](https://company.emart.com/en/main.do), this website is designed.