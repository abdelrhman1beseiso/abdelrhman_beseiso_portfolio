from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import VisitorMessage

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            message = form.save()
            
            # Send email
            send_mail(
                f"New message from {message.name}",
                message.message,
                message.email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # Reset form
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)

 

