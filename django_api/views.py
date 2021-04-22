from django.http import HttpResponse
from django.views import View

class BookViewSet(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')



from django.http import FileResponse, HttpResponse
from rest_framework.exceptions import ErrorDetail
import os
from django.conf import settings
from app.models import File
from django.utils.translation import gettext_lazy as _



def file_downloading(request, sid):
    """Return default image file"""
    try:
        file = File.objects.get(sid=sid)
        if file:
            return FileResponse(
                open(os.path.join(settings.MEDIA_ROOT, file.file_url.name), 'rb'),
                filename='test.ddd'
            )
    except:
        return HttpResponse(_("Phongtran"))


class Http401(HttpResponse):
    def __init__(self):
        super().__init__('401 Unauthorized', status=401)


from django.shortcuts import render

def Homepage(request):
    return render(request, 'test.html')

# def Unauthorized(request):
#     from app.tasks import sleepy, send_mail_task

#     result = send_mail_task.delay()

#     print(result.task_id)
#     # print(result.ready())
#     return HttpResponse('Unauthorized ' + result.task_id, status=403)

from django.contrib.auth.models import User


def StatusCelery(request):
    id = request.GET['id']
    from celery.result import AsyncResult
    res = AsyncResult(id)
    # res.ready()

    print('res.ready()', res.ready())

    print('res.info', res.info)
    print('res.status', res.status)
    print('res.state', res.state)

    return HttpResponse('Trang thai', status=403)


def SetCookie(request):
    res = HttpResponse('DONE', status=200)
    from random import random
    # res.delete_cookie('token')
    token = random()
    res.set_cookie('token', token)
    return res

def GetCookie(request):
    cookie = request.COOKIES
    return HttpResponse(f'GET COOKE {cookie}', status=200)
