from rest_framework import serializers
from .models import Student
from datetime import date

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    date_of_birth = serializers.DateField(required=True)  # 👈 Add this
    def validate_date_of_birth(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value
    class Meta:
        model = Student
        fields = '__all__'