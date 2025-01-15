from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Chat

@login_required
def chats(request):
    chats = Chat.objects.all()
    return render(request, 'chat/chats.html', {'chats': chats})