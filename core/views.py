# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from core.tools import TaskQueryFactoryMethod


def main_view(request):
    params = {}
    request_context = RequestContext(request)
    response = render_to_response('index.html', params, context_instance=request_context)
    return response


@require_GET
@csrf_exempt
def task_query(request, task_id):
    params = TaskQueryFactoryMethod(task_id=task_id).get_result()
    return HttpResponse(json.dumps(params), 'application/json')
