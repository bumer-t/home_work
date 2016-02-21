# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse


def response_error(message):
    response = HttpResponse(json.dumps({'message': message}), 'application/json')
    response.status_code = 500
    return response


def response_success(params):
    return HttpResponse(json.dumps(params), 'application/json')
