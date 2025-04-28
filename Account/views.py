from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, loginTable
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password


def userRegistration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Validate inputs
        if not username or not password or not password1:
            messages.error(request, 'All fields are required!')
            return redirect('Account:register')

        if password != password1:
            messages.error(request, 'Passwords do not match!')
            return redirect('Account:register')

        # Check if username exists
        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('Account:register')

        # Create user (with hashed password in real implementation)
        try:
            # In production, use make_password(password)
            userprofile = UserProfile.objects.create(
                username=username,
                password=password,  # Replace with make_password(password)
                password2=password1
            )
            
            login_table = loginTable.objects.create(
                username=username,
                password=password,  # Replace with make_password(password)
                password2=password1,
                type='user'
            )
            
            messages.success(request, 'Registration successful!')
            return redirect('Account:login')
            
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('Account:register')

    return render(request, 'user/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        

        if not username or not password:
            messages.error(request, 'Username and password are required!')
            return render(request, 'user/login.html')

        try:
            # In production, use check_password()
            user_details = loginTable.objects.get(username=username, password=password)
            
            request.session['username'] = user_details.username
            if user_details.type == 'admin':
                return redirect('Account:admin_view')
            else:
                return redirect('Account:user_view')

        except loginTable.DoesNotExist:
            messages.error(request, 'Invalid username or password!')
        except Exception as e:
            messages.error(request, f'Login error: {str(e)}')

    return render(request, 'user/login.html')

def admin_view(request):
    if 'username' not in request.session:
        messages.error(request, 'Please login first!')
        return redirect('Account:login')
    
    try:
        user_name = request.session['username']
        return render(request, 'listbook.html', {'user_name': user_name})
    except KeyError:
        return redirect('Account:login')

def user_view(request):
    if 'username' not in request.session:
        messages.error(request, 'Please login first!')
        return redirect('Account:login')
    
    try:
        user_name = request.session['username']
        return render(request, 'user/userinterface.html', {'user_name': user_name})
    except KeyError:
        return redirect('Account:login')

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('Account:login')

