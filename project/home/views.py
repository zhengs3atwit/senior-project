from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dashboard.models import UserRecord
import logging
logger = logging.getLogger(__name__)
from accounts.forms import CustomUserCreationForm

# Create your views here.

#homepage
def home(request):
    form = CustomUserCreationForm
    return render(request, 'index.html', {'the_register_form': form})


def malware(request):
    return render(request, 'campaigns/mal.html')


def credential(request):
    return render(request, 'campaigns/cred.html')


def spear(request):
    return render(request, 'campaigns/spear.html')


def fakelogin(request):
    return render(request, 'campaigns/fake.html')


# @csrf_exempt  
# def postmark_webhook(request):
#     print("appoles")
#     if request.method == 'POST':
#         try:
#             payload = json.loads(request.body)
#             logger.info(f"Webhook recieve: {payload}")
#             if payload.get('RecordType') == 'Click':
#                 print("potato")
#                 email = payload.get('Recipient', '')
#                 clicked_url = payload.get('OriginalLink', '')
#                 clicked_time = payload.get('ClickedAt', '')
#                 if email:
#                     print("aplesaucesasdasdada")
#                     user = UserRecord.objects.filter(email=email).first()
#                     if user:
#                         user.clicked = True
#                         user.email_click_time = clicked_time  
#                         user.save()
#                     else:
#                         logger.warning(f"No user found with email: {email}")
#             return JsonResponse({'status': 'ok'})
#         except json.JSONDecodeError:
#             logger.error("Invalid JSON received in webhook")
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     return JsonResponse({'error': 'Only POST allowed'}, status=405)

