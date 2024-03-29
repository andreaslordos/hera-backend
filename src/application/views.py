from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from application.models import Backup
import json
import uuid
import base64

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
            print("(request.POST['message'])")
            print(request.POST['message'])
            user.data = request.POST['message']
            user.save()
            return HttpResponse(json.dumps({ #send message back
                    'data': str(user.accessToken),
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
                print("returning user data: " + (user.data).replace(" ", "+"))
                #print(base64.b64decode(user.data, '-_'))

                returnUserData = (user.data).replace(" ", "+")
                success = 1
            return HttpResponse(json.dumps({
                    'data': returnUserData,
                    'success': success,
            }), 'application/json')
