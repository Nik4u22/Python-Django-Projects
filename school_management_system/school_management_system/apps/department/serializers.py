from rest_framework import serializers
from apps.department.models import Department

#Create serializers here
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    department_id = serializers.ReadOnlyField()
    class Meta:
        model = Department
        fields = "__all__"
        