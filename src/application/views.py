from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from application.models import Backup
import json
import uuid

def is_valid_uuid(val):
    try:
        return uuid.UUID(str(val))
    except ValueError:
        return None

@csrf_exempt # be able to receive request even if there is no CSRF token
def index(request):
    if (request.method == 'POST'):
        if (request.POST['type'] == "set"):
            user = Backup.objects.create()
            user.data = request.POST['message']
            user.save()
            return HttpResponse(json.dumps({ #send message back
                    'accessToken': str(user.accessToken),
                    'success': 1,
                }), 'application/json')
        elif (request.POST['type'] == "get"):
            returnUserData = None
            success = 0
            postedUUID = request.POST['message']
            print("posted uuid: " + postedUUID)
            checkedUUID = is_valid_uuid(postedUUID)
            print("checkeduuid: " + str(checkedUUID))
            user = Backup.objects.get(pk = checkedUUID)
            if (user != None):
                returnUserData = user.data
                success = 1
            return HttpResponse(json.dumps({
                    'data': returnUserData,
                    'success': success,
            }), 'application/json')
