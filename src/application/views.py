from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from application.models import Backup
import json

@csrf_exempt # be able to receive request even if there is no CSRF token
def index(request):
    if (request.method == 'GET'):
        user = Backup.objects.create()
        user.save()
        return HttpResponse(json.dumps({ #send message back
                'accessToken': user.accessToken.int,
                'data': "roLzT3GBhVQw22WrUPAdsw==",   
            }), 'application/json')
