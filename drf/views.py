from django.shortcuts import render
from .serializers import PeopleSerializer
from django.http import JsonResponse
from .models import People
from rest_framework.parsers import JSONParser
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
# Create your views here.

#authentication, authentication classes, viewsets & Routers


#using mixins & generic class based views
class genericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PeopleSerializer
    queryset = People.objects.all()
    lookup_field = 'id'
    def get(self, request, id):
        if id:
            return self.retrieve(request)
        return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.delete(request, id)


#using API classed based views(APIView)
class peopleAPIView(APIView):
    def get(self, request):
        people = People.objects.all() #Queryset
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)       

class detailAPIView(APIView):
    #To get pk
    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        people = self.get_object(pk) #Queryset
        serializer = PeopleSerializer(people)
        return Response(serializer.data)

    def put(self, request, pk):
        people = self.get_object(pk)
        serializer = PeopleSerializer(people, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        people = self.get_object(pk)
        people.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 

#using @api_view for function based views
@api_view(['GET', 'POST'])
def people(request):
    if request.method=='GET':
        people = People.objects.all() #Queryset
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, pk):
    people = People.objects.get(pk=pk)#instance
    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PeopleSerializer(people, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        people.delete()
        return HttpResponse(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def postoperation(request):
#     header = {"Access-Control-Allow-Origin":"*"}
#     x = int(request.data['x'])
#     y = int(request.data['y'])
#     operation = str(request.data['operation'])
#     split_str = operation.split(" ")
#     result = 0
#     add_array = ['add']
#     minus_array = ['minus']
#     mult_array = ['mult']
    
#     for items in split_str:
#         if items in add_array:
#             result = x+y
#             operation = "Addition"
#             break
#         elif items in minus_array:
#             result = x-y
#             operation = "Subtraction"
#             break
#         elif items in mult_array:
#             result = x*y
#             operation = "Multiplication"
#             break
#         else:
#             operation = "invalid operator"
#     new_data = {
#         "slackUsername":"Timmi",
#         "x":x,
#         "y":y,
#         "operation_type":operation,
#         "result":result,
#     }
#     return Response(new_data, status=status.HTTP_200_OK, headers=header)
