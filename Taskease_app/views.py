from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileImageForm
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    settings = models.Setting.objects.first()
    about = models.About.objects.all()
    whyus = models.Whyus.objects.all()
    service = models.Service.objects.all()
    callus = models.Callus.objects.first()
    helpers = models.Helpers.objects.all()
    faqs = models.Faq.objects.all()
    
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            # Handle the case where the profile doesn't exist
            profile = None  # Or create a new profile if needed, like:
            # profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if not request.user.is_authenticated:
            return redirect('Taskease_app-index')

        # FOR HIRING
        if form_type == 'hiring':
            hire_name = request.POST.get('hiring_name')
            hire_email = request.POST.get('hiring_email')
            hire_phone = request.POST.get('hiring_phone')
            hire_address = request.POST.get('hiring_address')
            hire_helper = request.POST.get('hiring_helper')
        

            hiring = models.Hiringform.objects.create(
                    full_name=hire_name,
                    email=hire_email,
                    phone=hire_phone,
                    home_address=hire_address,
                    helperid=hire_helper
                )
            hiring.save()
            return redirect('Taskease_app-payment-page') 

        # FOR CONTACTING
        elif form_type == 'contact':
            c_name = request.POST.get('client_name')
            c_email = request.POST.get('client_email')
            c_subject = request.POST.get('client_subject')
            c_message = request.POST.get('client_message')
            
            client = models.Contact.objects.create(
                client_name=c_name, 
                client_email=c_email, 
                client_subject=c_subject, 
                client_message=c_message)
            client.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('Taskease_app-index') 
        
        # FOR NEWSLETTER SUBSCRIPTION
        

    return render(request, 'Taskease_app/index.html', {'settings': settings, 'about':about, 'whyus':whyus, 'service':service, 'callus':callus, 'helpers':helpers, 'faqs': faqs,'profile': profile})

def innerpage(request):
    return render(request, 'Taskease_app/inner-page.html')
def portfoliodetails(request):
    return render(request, 'Taskease_app/portfolio-details.html')



def signuppage(request):
    settings = models.Setting.objects.first()
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Taskease_app/signup-page.html', {'settings': settings})

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'Taskease_app/signup-page.html', {'settings': settings})

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()
        
        messages.success(request, "Account created successfully!")
        return redirect('Taskease_app-signin-page')

    return render(request, 'Taskease_app/signup-page.html', {'settings': settings})



def signinpage(request):
    settings = models.Setting.objects.first()
    if request.method == 'POST':
        email = request.POST['email']  # Only accept email
        password = request.POST['password']

        # Attempt to authenticate the user using the email
        try:
            user = User.objects.get(email=email)
            username = user.username  # Get the username from the user object
            my_user = authenticate(request, username=username, password=password)

            if my_user is not None:
                login(request, my_user)
                messages.success(request, 'You are now logged in!')
                return redirect('Taskease_app-index')
            else:
                messages.error(request, 'Invalid email or password.')

        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'Taskease_app/signin-page.html', {'settings': settings})

def signout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('Taskease_app-index')

def paymentpage(request):
    settings = models.Setting.objects.first()
    profile = Profile.objects.get(user=request.user)
    return render (request, 'Taskease_app/payment-page.html',{'settings': settings, 'profile': profile})


@login_required
def profilepage(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # If the 'remove' button was clicked, remove the image
        if 'remove_image' in request.POST:
            profile.image = None  # Remove the image
            profile.save()
            return redirect('profile')  # Redirect to the profile page

        # If an image is uploaded via the form
        elif 'image' in request.FILES:
            form = ProfileImageForm(request.POST, request.FILES)
            if form.is_valid():
                profile.image = form.cleaned_data['image']  # Update the image field
                profile.save()  # Save the profile with the new image
                return redirect('profile')  # Redirect to the profile page

    else:
        form = ProfileImageForm(instance=profile)

    return render(request, 'Taskease_app/profile-page.html', {'form': form, 'profile': profile})


