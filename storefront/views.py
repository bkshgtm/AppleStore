from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django import forms

# Create your views here.
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# Your views
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})

def signupuser(request):
    if request.method == "GET":
        form = CustomUserCreationForm()  # Use the custom form here
        return render(request, 'signup.html', {'form': form})

    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Save the form, which creates the user
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': form, 'error': 'Enter a unique username'})
        else:
            return render(request, 'signup.html', {'form': form, 'error': 'Passwords didn’t match or other validation error'})

def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'login.html', {'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': form, "error": 'No such user found'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')








# def home(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {"products":products})

# def signupuser(request):
#     form = UserCreationForm()
#     if request.method == "GET":
#         return render(request,'signup.html', {'form':form})

#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('home')
#             except IntegrityError:
#                 return render(request, 'signup.html', {'error':'Enter an unique username'})
#         else:
#             return render(request,'signup.html',{'form':form, 'error':'Password didnt match'})


# def loginuser(request):
#     form = AuthenticationForm()
#     if request.method =='GET':
#         return render(request, 'login.html', {'form':form})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'login.html', {'form':form, "error":'No such user found'})
#         else:
#             login(request, user)
#             return redirect('home')
            
# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')







    