from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
# def home (request):
#     return HttpResponse("Hello, Django!!")
def home(request):
    name = request.GET['name']
    age = request.GET['age']
    getRequestDict = request.GET;
    # return JsonResponse(getRequestDict,encoder='utf-8')
    return JsonResponse(getRequestDict, encoder='utf-8')
 
