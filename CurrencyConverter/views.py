import json

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status
from CurrencyConverter.converter import convert


# Create your views here.
@api_view(["POST"])
def MoneyConvertView(req):
    try:
        body = json.loads(req.body)['query']
        return JsonResponse(convert(body), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
