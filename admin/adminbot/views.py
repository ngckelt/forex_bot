from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Clients


@login_required
def show_stat(request):
    clients = Clients.objects.all()
    amount = 0
    for client in clients:
        amount += client.deposit
    context = {
        "amount": amount,
    }
    return render(request, 'adminbot/stat.html', context=context)


