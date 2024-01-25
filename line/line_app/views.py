from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import create_message
from line_app.message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        events = request['events']
        for event in events:
            message = event['message']
            reply_token = event['replyToken']
            line_message = LineMessage(create_message.message(message['text']))
            line_message.reply(reply_token)
    return HttpResponse("ok")
