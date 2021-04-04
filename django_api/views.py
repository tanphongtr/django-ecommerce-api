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

    try:
        file = File.objects.get(sid=sid)
        if file:
            return FileResponse(
                open(os.path.join(settings.MEDIA_ROOT, file.file_url.name), 'rb'),
                filename='test.ddd'
            )
    except:
        return HttpResponse(_("Phongtran"))
