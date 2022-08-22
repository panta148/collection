from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def Home(request):
    if request.method == 'POST':
        to = request.POST.get('myemail')
        content = request.POST.get('content')
        print("Starting.................")
        send_mail("information", content, settings.EMAIL_HOST_USER, [to])
        messages.success(request, 'mail successfully send.')
        print(f"send successfully  to {to}")
        print("End.............")
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')
