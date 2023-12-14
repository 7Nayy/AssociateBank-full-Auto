from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def home(request):
    return render(request, 'registration/home.html',{'section' : 'home'})

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the choosen pwd
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Save the user object
            new_user.save()
            return render(request, 'registration/register_done.html',{'new_user' : new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'user_form' : user_form})