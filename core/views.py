from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from.forms import SignUpForm
# from .models import Message
# from django.contrib.auth.decorators import login_required


# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('frontpage')

# @login_required
# def chatroom(request, room_name):
#     messages = Message.objects.filter(sender=request.user) | Message.objects.filter(receiver=request.user)
#     return render(request, 'core/chatroom.html', {'room_name': room_name, 'messages': messages})