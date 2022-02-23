from rest_framework import views
from rest_framework.response import Response
from constance import settings, LazyConfig
from rest_framework.viewsets import ViewSet


config = LazyConfig()

def get_values():
    """
    Get dictionary of values from the backend
    :return:
    """

    # First load a mapping between config name and default value
    default_initial = ((name, options[0])
                       for name, options in settings.CONFIG.items())

    # Then update the mapping with actually values from the backend
    initial = dict(default_initial, **dict(config._backend.mget(settings.CONFIG)))
    
    return initial
class SettingAPIView(ViewSet):
    
    def get(self, request, *args, **kwargs):
        print(get_values(), '='*10)
        return Response(get_values(), )

    def create(self, request, *args, **kwargs):
        return Response(get_values(), )