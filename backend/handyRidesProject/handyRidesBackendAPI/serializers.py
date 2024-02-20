from rest_framework import serializers 
from .models import Person

class PersonSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Person
        fields = ["id", "name", "city", "state", "o_state", "o_city", "is_driver", "max_passengers", "price", "description"]  