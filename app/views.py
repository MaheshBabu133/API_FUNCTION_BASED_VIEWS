from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from app.serializers import *
from app.models import *
from rest_framework.response import Response
from rest_framework import status

@api_view()
def Empdata(request):
    EQS=Employee.objects.all() #list of all employee table objects
    ESD=EmpMS(EQS,many=True)
    return Response(ESD.data)