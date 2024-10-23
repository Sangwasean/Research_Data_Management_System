from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def user_view(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, 'User created successfully!')
            return redirect('user_view')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})  # Ensure t
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # Fetch the user based on the primary key
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)  # Bind form to the user instance
        if form.is_valid():
            form.save()  # Save the updated instance
            return redirect('user_view')  # Redirect to user list after saving
    else:
        form = UserForm(instance=user)  # If GET, create a form with the user instance
    return render(request, 'user_form.html', {'form': form})
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_view')
    return render(request, 'user_confirm_delete.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        # Get username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Debugging: Check if the POST request has the right data
        print(f"Username: {username}, Password: {password}")  # To see the input in the console

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in and redirect to the 'user_view'
            login(request, user)
            print("Login successful")  # Debugging: This will confirm successful login
            return redirect('user_view')  # Replace 'user_view' with the actual name of the view

        else:
            # If authentication fails, show an error message and stay on the login page
            print("Login failed: Invalid credentials")  # Debugging: This will confirm failed login
            messages.error(request, 'Invalid username or password.')  # Error message to show in the template
            return render(request, 'registration/login.html')  # Stay on the login page

    return render(request, 'registration/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page


@login_required
def user_view(request):
    # Your existing code to list users
    ...