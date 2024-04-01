from rest_framework import serializers
from .models import Employee, Address, WorkExperience, Qualification, Project


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_email(self, email_value):
        if self.instance:
            return email_value

        if Employee.objects.filter(email=email_value).exists():
            raise serializers.ValidationError("Email is already Exsist")
        return email_value
