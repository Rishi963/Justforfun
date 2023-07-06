from dataclasses import fields
from rest_framework import serializers
from .models import *

class testserials(serializers.ModelSerializer):
    class Meta:
        model =testmodel
        fields = '__all__'