from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Feature


# Create your views here.
def home(request):
    return HttpResponse("Hello World Example of PFSD Program")


def HomePage(request):
    return render(request, 'HomePage.html')


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Try to get the user by email
        try:
            username = User.objects.get(email=email).username  # Get the username associated with this email
        except User.DoesNotExist:
            messages.info(request, 'Credentials Invalid')
            return redirect('LoginPage')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('HomePage')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('LoginPage')
    else:
        return render(request, 'LoginPage.html')





def registerPage(request):
    if request.method == 'POST':
        username = request.POST['name']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email Already Used")
            return redirect('registerPage')  # Redirect to the correct URL
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already used')
            return redirect('registerPage')  # Redirect to the correct URL
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('LoginPage')  # After successful registration, redirect to login page
    else:
        return render(request, 'registerPage.html')



def Translator(request):
    return render(request, 'Translator.html')

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('HomePage')

def About_us(request):
    return render(request,'About_us.html')

def services(request):
    return render(request,'services.html')

def Shedule(request):
    return render(request,'Shedule.html')

def LearnHomePage(request):
    return render(request,'LearnHomePage.html')

def Books(request):
    return render(request,'Books.html')