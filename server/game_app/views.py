from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from game_app.models import User
#from game_app.serializers import UserSerializer
#from rest_framework import generics
#from permissions import IsAuthenticatedOrCreate

# Create your views here.
#def user_list():
#	user = User.objects.all()
	#serializer = UserSerializer(user, many=True)
	#return JsonResponse(user[1].username,safe=False)


def index (request):
	return HttpResponse("Hii")
