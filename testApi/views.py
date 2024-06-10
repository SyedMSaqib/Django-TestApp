from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employee
from .serializers import EmployeeSerializer
from rest_framework import status

def index(req):
    return HttpResponse("Hello world")

@api_view(['GET'])
def get_all_employees(req):
    Employee=employee.objects.all()
    serializer=EmployeeSerializer(Employee,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_employees(req):
    serializer=EmployeeSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




