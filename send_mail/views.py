import os
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SendForm
from django.core.mail import send_mail, BadHeaderError

def home(request):
    if request.method == "POST":
        form = SendForm(request.POST)
        if form.is_valid():
            subject = 'Message from TestAccount'
            message = form.cleaned_data['content']
            sender = form.cleaned_data['email']
            recipients = os.getenv('TO_EMAIL')
            try:
                send_mail(subject, message, sender, [recipients], fail_silently=False)
                return HttpResponse('Successfully sent a message!')
            except BadHeaderError:
                return HttpResponse('Error!')
    else:
        form = SendForm()
    return render(request, 'send_test/home.html', {'form':form })