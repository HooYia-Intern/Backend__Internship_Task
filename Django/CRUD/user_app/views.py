from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def home(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        elif 'update_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('home')
        elif 'delete_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return redirect('home')

    users = User.objects.all()
    create_form = UserForm()

    context = {
        'users': users,
        'create_form': create_form,
    }

    # Add a form for each user
    for user in users:
        context[f'user_update_form_{user.id}'] = UserForm(instance=user)

    return render(request, 'home.html', context)

# Update user view (optional if needed separately)
def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_update.html', {'form': form, 'user': user})

# Delete user view
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'user_confirm_delete.html', {'user': user})
