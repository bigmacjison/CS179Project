from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from AniModels.models import User, Pet
from AniModels.serializers import UserSerializer, PetSerializer
from django.template import loader
from django.shortcuts import render


class UserList(APIView):
    #List all users, or create a new user
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PetList(APIView):
    #List all pets, or create a new pet
    def get(self, request, format=None):
        petss = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class UserDetail(APIView):
    #Retrieve, update or delete a user instance
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class PetDetail(APIView):
    #Retrieve, update or delete a pet instance
    def get_object(self, pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pet = self.get_object(pk)
        serializer = PetSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pet = self.get_object(pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
#@csrf_exempt
@api_view(['GET','POST'])
def user_list(request, format=None):
    #List all users or creat a new User
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = UserSerializer(data=data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.error, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#@csrf_exempt
@api_view(['GET','POST'])
def pet_list(request, format=None):
    #List all pets or creat a new Pet
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = PetSerializer(data=data)
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.error, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    #Retrieve, update or delete a user
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = UserSerializer(user)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        #serializer = UserSerializer(user, data=data)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.error, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        user.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])        
def pet_detail(request, pk, format=None):
    #Retrieve, update or delete a pet
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = PetSerializer(pet)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        #serializer = PetSerializer(user, data=data)
        serializer = PetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.error, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        pet.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

def index(request):
    all_users = User.object.all()
    template = loader.get_template('polls/index.html')
    context = {'all_users': all_users}
    #output = ', '.join([u.first_name for u in all_users])
    #return HttpResponse(template.render(context, request))
    return render(request, 'AniModels/index.html', context)