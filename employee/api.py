from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from employee.serializers import *
import copy

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class InfoList(APIView):
    def get(self,request):              #Overriding HTTP Methods 
        name = request.GET.get("employee_name")
        id = request.GET.get("employee_id")
        if name:
            name = name.replace('\"','')
            model_name = Info.objects.filter(employee_name=name)
        if id:
            model_id = Info.objects.filter(employee_id=id)
        if id and name:
            emp_name = model_id.values_list("employee_name")[0]
            if str(emp_name[0]) not in str(model_name):
                return Response("Cannot Find Any record for given employee_name and employee_id",status=status.HTTP_400_BAD_REQUEST)
            else:
                model = model_id
        elif id:
            model = model_id
        elif name:
            model = model_name  
        else:
            model = Info.objects.all()
        serializer = InfoSerializer(model, many=True)
        return Response(serializer.data) 

    def post(self,request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfoDetail(APIView):
    def get_model(self,employee_id):
        try:
            model = Info.objects.get(employee_id=employee_id)
            return model
        except:
            return 0

    def get(self,request,employee_id):
        model = self.get_model(employee_id)
        if model == 0:
            return Response(f'User with Employee id {employee_id} Does Not Exist', status=status.HTTP_404_NOT_FOUND )
        serializer = InfoSerializer(model)
        return Response(serializer.data)

    def put(self,request,employee_id):
        model = self.get_model(employee_id) 
        if model == 0:
            return Response(f'User with Employee id {employee_id} Does Not Exist', status=status.HTTP_404_NOT_FOUND )
       # newage = request.data.get("age")
       # model = Info.objects.filter(id=employee_id).update(age=int(newage))
        serializer = InfoSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       # return Response("record Updated", status=status.HTTP_200_OK)
   
    def delete(self,request,employee_id):
        model = self.get_model(employee_id) 
        if model == 0:
            return Response(f'User with Employee id {employee_id} Does Not Exist', status=status.HTTP_404_NOT_FOUND )
        model.delete()
        return Response("Record Deleted", status=status.HTTP_200_OK)