# -*- coding: utf-8 -*-
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from core.tools import TaskQueryFactoryMethod
from core.tools.task_1 import TreeHelper, Node


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


@require_GET
@csrf_exempt
def task_1(request):
    helper_tree = TreeHelper()
    tree = helper_tree.create()
    print_1 = helper_tree.print_values(t=tree, slug='PRINT_1')

    tree_str = tree.serialize()

    new_tree = Node.decode(tree_str)
    print_2 = helper_tree.print_values(t=new_tree, slug='PRINT_2')

    params = {'print_1':print_1,'print_2':print_2}
    return HttpResponse(json.dumps(params), 'application/json')
