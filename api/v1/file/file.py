from os import name
from rest_framework import generics, status
from app.models import File
from .serializers import FileSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework import permissions
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.utils.translation import get_language_from_request, activate
from django.middleware.locale import LocaleMiddleware as _

from django.conf import settings
from django.conf.urls.i18n import is_language_prefix_patterns_used
from django.utils import translation
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination

class PageNumberPagination(_PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10

class LocaleMiddleware(_):
    def process_request(self, request):
        urlconf = getattr(request, 'urlconf', settings.ROOT_URLCONF)
        i18n_patterns_used, prefixed_default_language = is_language_prefix_patterns_used(urlconf)
        language = translation.get_language_from_request(request, check_path=i18n_patterns_used)
        language_from_path = translation.get_language_from_path(request.path_info)
        if not language_from_path and i18n_patterns_used and not prefixed_default_language:
            language = settings.LANGUAGE_CODE
        translation.activate(language)
        language, is_authenticated = request.user
        if is_authenticated:
            language = ''

        request.LANGUAGE_CODE = translation.get_language()



class FileAPIView(generics.ListCreateAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = PageNumberPagination

    parser_classes = (MultiPartParser,)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class FileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'sid'
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        # request.session[LANGUAGE_SESSION_KEY] = 'en'
        language = get_language_from_request(request)

        print(language)

        activate('vi')
        return super().get(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    # def get_object(self):
    #     try:
    #         return self.filter_queryset(self.get_queryset().filter(sid=self.kwargs.get('sid')))
    #     except:
    #         raise