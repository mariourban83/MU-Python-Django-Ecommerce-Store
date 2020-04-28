[![Build Status](https://travis-ci.com/mariourban83/milestone4-eshop.svg?branch=master)](https://travis-ci.com/mariourban83/milestone4-eshop)

## Ecommerce Django-Python project.
[![LR Onlineshop Demo](https://eshop-static-s3.s3-eu-west-1.amazonaws.com/static/img/git_banner_1.jpg "LR-Onlineshop Demo")](https://lr-onlineshop.herokuapp.com)

---

## Table of Contents
* [Project summary](#project-summary)
* [Design](#design)
* [User Experience](#ux)   
    * User Stories
* [Features](#features)
    * Existing Features
    * Features to be implemented
* [Technologies used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
    * Local deployment
    * Heroku
* [Credits](#credits)

---
## [Project summary](#project-summary)

Full Stack Framework website project with Python 3.7 and Django 3.

1. The goal of this project is to create a simple yet fully functional e-commerce website selling German health supplements, first class Aloe Vera products and cosmetics.
2. Build simple, reusable django ecommerce app that can be used as an template and reference again in the future projects.
3. Fulfill Customer ( [Code Institute - Europe's leading online bootcamp](https://codeinstitute.net/full-stack-software-development-diploma/ )) requirements of final milestone project.

---

## [Design](#design)
The website was designed with mobile first approach with user in mind. The wirefames with first design can be found [here](https://xd.adobe.com/view/f4ff46c1-8646-438f-7674-4707e14ed56d-82ce/).    

The project uses Poppins and Roboto fonts from Google Fonts Library
Main color #74ab8c  is used for topbar and footer.The color was chosen to match with product collection color.

[![User flow](https://eshop-static-s3.s3-eu-west-1.amazonaws.com/static/img/User+Flow.png "User Flow")](https://lr-onlineshop.herokuapp.com)

---  

## [User Experience](#ux)   

### User Stories  

'Simplicity, usability with elegance to meet exact needs of customer.'

#### As a shopper, user I expect:  

* Browse products within the store
* Filter the products by category
* Search product or info
* Add products to the cart
* View and modify cart
* Apply discount codes
* Go through simple secured checkout proccess
* Be able to place order with or without the account
* To have an options for paying for the order 
* Register an account
* Login to dashboard to modify personal info
* See status of the recent order(dispatched?)
* See order history
* Print invoice
* Find contact info
* Get notifications about actions on the website and also via email regarding the orders

#### As an administrator I want:  
* Be able to login to dashboard where I can find info about
    * Customers
    * Orders  
    * Status of orders
* See and print Invoices
* Bee able to export orders as csv
* Be able to add, edit or remove orders
* Edit customers info
* Contact customers  

[Back to top](#project-summary)

---  

## [Features](#features)

### Existing Features

#### Global

* Topbar with logo - Full page width container with logo linking to the home page.
* Search bar - available on all pages able to query string in the whole database and display the results on the search.html page
* Responsible navbar:
    * On larger screen display the links from the left and accounts dropdown with cart status on the right
    * On smaller screen display hamburger icon for puldown menu with links on the left and cart and accounts dropdown menu on the right
* Cart displaying current amount of items in cart, linked to cart detail page
* Account access dropdown menu for register,login, logout and dashboard view. For NOT logged in user, it displays link to login or register page, for logged in users, logout and dashboard view and personal message.
* Footer with
    * Section for displaying quick links and
    * Section with store opening hours and contact information(linked to email or phone app)

#### Home page

Simple page with some graphics displaying bestselling products. Products displayed here are filtered based on attribute 'bestseller', specified in the models and editable within admin area. Her, user has an option to add product to the card without specifiyng quantity.This page can be also used for announcements, news, updates.

#### Special offer

Page displaying products filtered based on attribute 'special_offers'.

#### Products page

Main Product list page. This page lists all products available within the store. Each product is placed in the container linked to the product detail page. Each container contains product name, image, content, price and form for adding chosen amount of item to the cart. After clicking on add to cart button, product/s is/are added to the cart und user is transfered to the cart view page. This acts also as a confirmation that the product/s been added to the cart.   
After clicking on the container with the product, user gets redirected to the detail page of the product.
On this page, category filter, located above all products, can be applied to display all or filtered by 'category' products.

#### Product detail page

After selecting amount and pressing add to cart button, user is redirected to the cart page

#### Categories Page

Displaying only products in selected category.

#### Search Page

Full site search is performed after entering string into the searchbar box. User is redirected to the search result page where relevant results are displayed

#### Cart

If cart is empty, only 'Cart is empty is displayed'. After adding an item to the cart(clicking add to cart button), user gets redirected to the cart page where products present in cart are displayed on the left with the ability to update ammount of product/s or remove the item/s completely from the cart. Price is automatically calculated after add, edit or remove item/s (user actions).

#### Checkout
Currently, if user is not logged in, after clicking on checkout button on cart page, user is redirected to the page where log in or continue as guest checkout options are displayed. This is giving user freedom to choose to buy items without registering an account.
* Clicking here on sign in link will redirect user to the sign in page. Items in cart persist after succesfull login. 
* Clicking on continue as guest will redirect to the order create page where user is required to fill in  personal details.

#### Order Create
User is presented with order form where details like address, name, etc are required to place an order and to continue to payment page.

#### Payment page
User is presented with the option to select either stripe or paypal as payment gateway. Clicking on stripe pay now button will open stripe payment form in new window where correct credit card details are required before they're submitted. If details are correct, payment is processed, and user is redirected to the custom payment_success page.

#### Login, Logout, Register, Dashboard
Standard django forms and sessions are used for managing user accounts

#### Admin area
* Option to export orders in the csv format
* Ability to export individual order in the PDF format

### Features to be implemented
* Sending emails from the app to the customer
* Recommendation engine for displaying popular and frequently bought items
* Customer dashboard to be populated with personal details, recent orders, invoices
* Full PayPal integration
* Testing
---

[Back to top](#project-summary)

---  

## [Technologies used](#technologies-used)

Folowing programming languages, technologies, libraries and tools were used for building the project:

- [Python 3.7.4](https://www.python.org/)
- [Venv Virtual environment](https://docs.python.org/3/library/venv.html)
- [Django 3.0.4](https://www.djangoproject.com/)
- [GitHub](https://github.com/)
- [Travis](https://travis-ci.org/)
- [Heroku](https://www.heroku.com/)
- [VS Code](https://code.visualstudio.com/)
- [AWS S3](https://aws.amazon.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQlite3](https://www.sqlite.org/index.html)
- HTML
- CSS
- JavaScript
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Adobe XD](https://xd.adobe.com/)
- [Stripe](https://stripe.com)
- [Paypal](https://paypal.com)

---

## [Testing](#testing)
Google Chrome's and Firefox's Development tools on local pc were constantly used to test changes I
made to project and to make sure its displaying correctly on all screen sizes.
I also used different mobile devices like phones, tablets and iPads for checking correct mobile responsivennes.

For code Validation:  
      
Forms and inputs are validated by django itself.    
Pep8 linter was helpful by highlighting syntax errors during development.    

---

## [Deployment](#deployment)

For my version control I used Github and Heroku for hosting the live project.

#### For local deployment: 

1. Open Terminal in the desired project directory of local maschine
2. Create and activate virtual environment if necessary.   
  ```python3 -m venv venv ```   
  ```source venv/bin/activate``` for linux maschine.
3. Enter folowing commands :   
```git clone https://github.com/mariourban83/milestone4-eshop.git ```  (will download and unpack the project)   
```pip3 install -r requirements.txt```
4. In the main project folder of the project directory, where settings.py lives, create  **.env** file and enter the following:

* SECRET_KEY = "your own key"  # Django app secret key
* AWS_ACCESS_KEY_ID = "your own key"  # Amazon S3 
* AWS_SECRET_ACCESS_KEY = "your own key"  # Amazon S3
* STRIPE_SECRET_KEY = "your own key"  # Stripe
* STRIPE_PUBLISHABLE_KEY = "your own key"  # Stripe
* DATABASE_URL = "your own key"  # Postgres key from Heroku
* CLIENT_ID = "your own key"  #Paypal    
Replace the **"your own key"** value with your secret keys 

6. In the terminal, enter the folowing commands : 
* ``python manage.py makemigrations``
* ``python manage.py migrate``
* ``python manage.py createsuperuser``
* ``python manage.py runserver``    

In the browser, open http://127.0.0.1:8000  and the project should be now live and ready to use.


#### To deploy the project to Heroku

1. Create the app in Heroku.
2. Add ***Heroku Postgres*** free ***Hobby*** level in the ***Add-Ons*** section for serving postgres database.
3. Copy all variables (keys) from the  ***.env***  file located in the root folder of the project directory to the ***Config Vars*** section in Heroku->Project->Settings.
5. In Heroku->Project->Deploy section connect the github repository of the project and ***Enable Automatic Deploys*** from the master branch if thats the case. Otherwise, manual Deploy Branch option is available too.
5. Before Deploying the Branch, ***Procfile*** and updated ***requirements.txt*** files are necessary to be in the root dir of the folder.
6. If automatic deploys were selected, from now on the project updates after every commit to github.
7. If Deployement, build, went successfuly, restart the dynos in Heroku -> Project Section and project.
8. Allowed Hosts section in settings.py file should now be updated in order to serve the website.(Add deployed heroku project website address to the python ```ALLOWED_HOSTS``` dictionary ).
9. The project should be now visible to the public on the https address Heroku provides.    


The live version of this project deployed to Heroku can be found [here](https://lr-onlineshop.herokuapp.com/).

---

[Back to top](#project-summary)

## [Credits](#credits)

#### Content

Product images used from the official product catalog of the company.    
Banners and graphics created by myself using Pixabay and Canva.  
Product description used from product cataloque

#### Inspiration & Sources  

Code Institute Ecommerce project    
Django Official Website    
Youtube videos and Udemy courses    
Django related books    

#### Thanks

To Code Institute for providing this oportunity to learn web development in a well structured and supportive way.
To my mentor, Seun Owonikoko for her kind support.
To my amazing wife, for supporting and encouraging me on my developer journey

### For Educational Use Only

[Back to top](#summary)
