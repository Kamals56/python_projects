from django.shortcuts import render
from django.http import HttpResponse



def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side </p>")

import json
from .responses import bot_response

def get_chat_response(request, slug=None):
    data = request.GET
    message = data.get("message")
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))