from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


from user.forms import LoginForm, RegisterForm


# Create your views here.
def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd["email"]
            password = cd["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "You are now logged in")
                return redirect('products:list')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('user:login_page')

    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You are now registered")
            login(request, user)
            return redirect('products:list')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('products:list')