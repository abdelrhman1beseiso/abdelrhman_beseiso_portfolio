from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import resend
import os

# It's better practice to get the API key from settings.py, especially for production.
# For local testing, you can keep the hardcoded key for now,
# but for deployment, use environment variables or Django settings.
# Ensure you have RESEND_API_KEY defined in your settings.py if you uncomment the line below:
# resend.api_key = settings.RESEND_API_KEY 
resend.api_key = "re_T688dGfy_3pEBNwwsSaEobur8HxfRU6xL"

def home(request):
    """
    Renders the main portfolio index page.
    This view should only handle GET requests to display the page.
    """
    return render(request, 'portfolio/index.html')

def send_message(request):
    """
    Handles the AJAX POST request for sending contact messages via Resend.
    This view specifically processes the form submission from the modal.
    """
    # Ensure it's an AJAX POST request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            # Basic validation
            if not all([name, email, message]):
                return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
            
            # More robust email format validation can be done with Django Forms
            if "@" not in email or "." not in email:
                return JsonResponse({'status': 'error', 'message': 'Please enter a valid email address.'}, status=400)

            resend.Emails.send({
                "from": "Acme <onboarding@resend.dev>", # Ensure this is a verified sender in Resend
                "to": "abdelrhman.f.beseiso@gmail.com",  # Your recipient email address
                "reply_to": email,
                "subject": f"New Portfolio Message from {name}",
                "html": f"""
                    <h3>New Portfolio Message</h3>
                    <p><strong>From:</strong> {name} ({email})</p>
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                """
            })
            return JsonResponse({'status': 'success', 'message': 'Your message was sent successfully!'})
        
        except Exception as e:
            # Log the error for debugging purposes (e.g., using Django's logging)
            print(f"Error sending email: {e}") 
            return JsonResponse({'status': 'error', 'message': f'Failed to send message: {str(e)}'}, status=500)
    
    # If it's not an AJAX POST request, or not a POST request at all,
    # return an appropriate error. This prevents direct access to /send-message/ via GET.
    return JsonResponse({'status': 'error', 'message': 'Invalid request method or not an AJAX request.'}, status=400)