from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return HttpResponse("Hello, World!")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat_page')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

@login_required
def welcome_view(request):
    return render(request, 'chat/welcome.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_page(request):
    messages = ChatMessage.objects.order_by('timestamp').all()[:50]
    return render(request, 'chat/chat_page.html', {'messages': messages})

def test_page(request):
    return render(request, 'chat/test.html')
