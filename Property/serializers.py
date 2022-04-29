from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Property.models import *

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class GetDataSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class GetContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
    
    def create(self, validated_data):
        return ContactUs.objects.create(**validated_data)
       