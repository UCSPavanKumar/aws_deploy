from typing import Any
from .models import AccessLogModel
from django.conf import settings
from django.utils import timezone

class AccessLogMiddleWare(object):
    def __init__(self,get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.session_key:
            request.session.create()
        
        access_log_data = dict()

        access_log_data['path'] = request.path
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        access_log_data['ip_address'] = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        access_log_data['method'] = request.method
        access_log_data['referrer'] = request.META.get('HTTP_REFERER',None)
        access_log_data['session_key'] = request.session.session_key

        data = dict()
        print(access_log_data)
        data['get'] = dict(request.GET.copy())
        data['post'] = dict(request.POST.copy())
        keys_to_remove = ['password','csrfmiddlewaretoken']
        access_log_data['timestamp'] = timezone.now()

        try:
            AccessLogModel(**access_log_data).save()
        except Exception as e:
            print(str(e))

        response = self.get_response(request)
        return response