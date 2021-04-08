from rest_framework import response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # print(response.data)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

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