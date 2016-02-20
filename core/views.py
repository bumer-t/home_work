# -*- coding: utf-8 -*-
import json
from django.db import connection
from django.db.models import Count
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from core.models import User


def main_view(request):
    params = {}
    request_context = RequestContext(request)
    response = render_to_response('index.html', params, context_instance=request_context)
    return response


@require_GET
@csrf_exempt
def task_3(request):
    MAX_COUNT = 3

    if not User.objects.all().exists():
        HttpResponse(json.dumps({'message': 'ERROR: DB is EMPTY'}), 'application/json')

    cursor = connection.cursor()
    sql = "SELECT a.id, a.name, a.data  FROM  core_user a LEFT  JOIN (SELECT id, COUNT(name) FROM core_user GROUP BY name HAVING COUNT(name) >= %s LIMIT 1)  b on a.id = b.id LIMIT 1" % MAX_COUNT
    cursor.execute(sql)

    users = User.objects.filter().values('name').annotate(count_id=Count('name')).order_by('count_id').filter(count_id__gte=MAX_COUNT)
    params = {
        'cursor_result' : cursor.fetchall(),
        'orm_result'    : User.objects.filter(name=users[0]['name'])[0].output,
    }
    return HttpResponse(json.dumps(params), 'application/json')
