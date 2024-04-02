from django.shortcuts import get_object_or_404
from api.models import Employee
from .serializers import (
    EmployeeSerializer,
    AddressSerializer,
    ProjectSerializer,
    QualificationSerializer,
    WorkExperienceSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import *


class EmployeeapiViewset(ViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        employee_data = request.data
        address_data = employee_data.pop("address_details", None)
        work_experience_data = employee_data.pop("work_experience", [])
        qualifications_data = employee_data.pop("qualifications", [])
        projects_data = employee_data.pop("projects", [])
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
        else:
            return Response(
                employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
        else:
            return Response(
                address_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        work_experience_serializer = WorkExperienceSerializer(
            data=work_experience_data, many=True
        )
        if work_experience_serializer.is_valid():
            work_experience_serializer.save()
        else:
            return Response(
                work_experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        qualification_serializer = QualificationSerializer(
            data=qualifications_data, many=True
        )
        if qualification_serializer.is_valid():
            qualification_serializer.save()
        else:
            return Response(
                qualification_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        project_serializer = ProjectSerializer(data=projects_data, many=True)
        if project_serializer.is_valid():
            project_serializer.save()
        else:
            return Response(
                project_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"message": "Sucessfully created ", "data": employee_serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):

        try:
            employee_instance = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(
                {"detail": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )

        employee_data = request.data

        address_data = [employee_data.pop("address_details", None)]
        work_experience_data = employee_data.pop("work_experience", [])
        qualifications_data = employee_data.pop("qualifications", [])
        projects_data = employee_data.pop("projects", [])

        employee_serializer = EmployeeSerializer(
            instance=employee_instance, data=employee_data, partial=True
        )
        if not employee_serializer.is_valid():
            return Response(
                employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        employee_serializer.save()

        if address_data:
            Address.objects.filter(employee=employee_instance).delete()
            address_serializer = AddressSerializer(data=address_data, many=True)
            if address_serializer.is_valid():
                address_serializer.save()
            else:
                return Response(
                    address_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        if work_experience_data:
            a = employee_instance.workexperience_set.first()
            WorkExperience.objects.filter(employee=employee_instance).delete()
            work_experience_serializer = WorkExperienceSerializer(
                data=work_experience_data, many=True
            )
            if work_experience_serializer.is_valid():
                work_experience_serializer.save(employee=employee_instance)
            else:
                return Response(
                    work_experience_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if qualifications_data:
            Qualification.objects.filter(employee=employee_instance).delete()
            qualification_serializer = QualificationSerializer(
                data=qualifications_data, many=True
            )
            if qualification_serializer.is_valid():
                qualification_serializer.save(employee=employee_instance)
            else:
                return Response(
                    qualification_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if projects_data:
            Project.objects.filter(employee=employee_instance).delete()
            project_serializer = ProjectSerializer(data=projects_data, many=True)
            if project_serializer.is_valid():
                project_serializer.save(employee=employee_instance)
            else:
                return Response(
                    project_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        return Response(
            {
                "message": "Sucessfully updated",
                "employee": EmployeeSerializer(employee_instance).data,
            },
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, pk=None):
        try:
            employee_instance = Employee.objects.get(id=pk)

        except Employee.DoesNotExist:
            return Response(
                {"detail": "Employee not found"}, status=status.HTTP_404_NOT_FOUND
            )
        employee_instance.delete()

        return Response({"message": "successfully deleted"}, status=status.HTTP_200_OK)
