from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
    return render(request, 'app/index.html', {})

def hello(request):

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('global',
            {
                'type': 'global.receive',
                'message': 'hello',
            }
    )

    return HttpResponse(status=HTTPStatus.CREATED)
