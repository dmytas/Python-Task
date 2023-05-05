from rest_framework import serializers
from .models import Menu_of_day


class Menu_of_daySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_of_day
        fields = '__all__'
