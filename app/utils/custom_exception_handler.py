from rest_framework import response
from rest_framework.views import set_rollback
from rest_framework import exceptions, status
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            # print('==========================================================>')
            # print(exc)
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # print(exc, context)
    # print('======================================')
    # print(context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response

    return response


from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    # status_code = 503
    # default_detail = 'Service temporarily unavailable, try again later.'
    # default_code = 'service_unavailable'

    # status_code = 400
    # _message = 'API error, try again later.'
    # _message_code = '00000'

    # def __init__(self, message=None, message_code=None,
    #              detail=None, root_exception=None, response=None):
    #     self.message = self._message if not message else message

    #     if not response:
    #         response = {
    #             'message': self.message,
    #         }
    #         if not detail:
    #             detail = {}
    #         response['errors'] = detail
    #     super().__init__(detail=response, code=message_code)

    pass