from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


def apiOverView(request):
	return JsonResponse("API BASE POINT", safe=False)