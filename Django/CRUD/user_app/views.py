from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after saving
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form, 'action': 'Add'})

def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after saving
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'action': 'Edit'})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('home')  # Redirect to home page after deleting
    return render(request, 'user_confirm_delete.html', {'user': user})
