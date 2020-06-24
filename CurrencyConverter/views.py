import json

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status
from CurrencyConverter.converter.MyParser import MyParser


@api_view(["POST"])
def money_convert_view(req):
    """
    View who handles the api route /money/convert
    usages:

    POST /money/convert
    {
    "query": "10.32 EUR en USD"
    }

    HTTP/1.1 200 OK
    {
    "answer": "10.32 EUR = 11.30 USD"
    }
    """
    try:
        parser = MyParser()
        body = json.loads(req.body)['query']
        return JsonResponse(parser.convert(body), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
