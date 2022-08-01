from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from application.models import Backup
import json

@csrf_exempt # be able to receive request even if there is no CSRF token
def index(request):
    if (request.method == 'POST'):
        if (request.POST['type'] == "set"):
            user = Backup.objects.create()
            user.data = request.POST['message']
            user.save()
            return HttpResponse(json.dumps({ #send message back
                    'accessToken': str(user.accessToken.int),
                    'success': 1,
                }), 'application/json')
        elif (request.POST['type'] == "get"):
            user = Backup.objects.get(pk = request.POST['accessToken'])
            return HttpResponse(json.dumps({
                    'data': user.data,
                    'success': 1,
            }), 'application/json')
