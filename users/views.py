from django.shortcuts import render, redirect
from django.contrib import messages  # for message alerts
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm  #inheriting forms.py for user creation
from .forms import UserUpdateForm, ProfileUpdateForm  #for profile update


# Create your views here.
def register(request):
    if request.method == 'POST':  #checks if http request is POST type
        #create a form instance with data from POST
        form = UserRegisterForm(request.POST)
        if form.is_valid():  #check form validity
            form.save()  #saves user into Users database

            #grab username from form
            username = form.cleaned_data.get('username')
            #generate message on successfull creation
            messages.success(
                request,
                f'Your account has been created! Please login to continue.')
            return redirect('login')  #redirect to homepage

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#decorator to add login required fxnality in case user tries to access /profile when not logged in
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/profile.html', context)
