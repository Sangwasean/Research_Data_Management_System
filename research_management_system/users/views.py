from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .models import CustomUser
def user_view(request):
    return render(request, 'index.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Use CustomUser here
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user object but don't save yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the database

            messages.success(request, 'User created successfully!')
            return redirect('users')  # Redirect to the users page or any other page
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})  # Ensure t
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to user list after saving
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('users')  # Redirect to user list after deletion
    return render(request, 'user_confirm_delete.html', {'user': user})
