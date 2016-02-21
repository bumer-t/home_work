# -*- coding: utf-8 -*-
import json
import traceback
from django.http.response import HttpResponse
from core.tools.response_helper import response_error
from functools import wraps
from settings import DEBUG


def api_view_500(output=None):
    def decorator(view_func):
        @wraps(view_func)
        def inner(request, *args, **kwargs):
            try:
                response = view_func(request, *args, **kwargs)
            except AssertionError as e:
                return response_error(unicode(e.args[0]))
            except Exception as ex:
                logger_error = {
                    'func_name'         : view_func.func_name,
                    'module'            : 'api_view_500',
                    'request_body'      : request.body if hasattr(request, 'body') else 'empty',
                    'request_post'      : request.POST,
                    'request_get'       : request.GET,
                    'message_error'     : str(ex),
                }
                #todo logger(logger_error)
                if DEBUG:
                    print logger_error
                    print traceback.format_exc()
                    raise ex
                if output == 'json_400':
                    return HttpResponse(json.dumps({"err": "Unknown error.", "code": 400}))
                return response_error(u'Непредвиденная ошибка')
            return response
        return inner

    return decorator
