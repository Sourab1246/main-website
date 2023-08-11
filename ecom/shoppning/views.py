from django.shortcuts import render,redirect
from .models import Products
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    products=Products.objects.all()
    return render(request,'shoppning/home.html',{'products':products})

   
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the homepage after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'shoppning/register.html', {'form': form})
        

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('home')

            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage after successful login
            else:
                # Display an error message for invalid credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
   
    return render(request,'shoppning/login.html',{'form':form}) 

def profile(request):
    return render(request,'shoppning/profile.html')  

def product_detail(request,product_id):
        return render(request,'shoppning/product_detail.html',{'product': product})

def cart(request):
    return render(request,'shoppning/cart.html')   

def checkout(request):
    return render(request,'shoppning/checkout.html')

def order_confirmation(request):
    return render(request,'shoppning/order_confirmation.html')

