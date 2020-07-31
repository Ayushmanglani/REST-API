from rest_framework import serializers
from employee.models import Info

#Serializing model
class InfoSerializer(serializers.ModelSerializer):
    employee_id = serializers.IntegerField(required=False)
    employee_name = serializers.CharField(required=False)
    class Meta:
        model = Info
       # fields = '__all__'                                      #for all fields
        fields = ('employee_name','employee_id','age')           #for Specific fields   