from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status  
from rest_framework import generics 
from Property.serializers import *
from Property.models import *

# Create your views here.
class GetStateView(APIView):
    def get(self, request, format=None):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)


class GetCityView(APIView):
    def get(self, request, format=None):
        state = City.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)


class GetDataView(APIView):
    def get(self, request, name, format=None):
        property = Property.objects.filter(category__name="%s" % name)
        serializer = GetDataSerializer(property, many=True)
        return Response(serializer.data)
        

class GetContactUsView(APIView):
    def get(self,request,format=None):
        contactus = ContactUs.objects.all()
        serializer = GetContactUsSerializer(contactus, many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = GetContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   