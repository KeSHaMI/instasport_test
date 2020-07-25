from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Workout
from .serializers import UserSerializer, WorkoutSerializer
from .forms import UserForm
# Create your views here.

class Register(APIView):

	def post(self, request):

		serializer = UserSerializer(data=request.data) 
		
		if serializer.is_valid():
			serializer.save()
			
			return Response(serializer.data, status=200)
		else:
			return Response(serializer.errors, status=400)

class Login(APIView):


	def post(self, request):

		email = request.data.get('email')
		password = request.data.get('password')

		user = authenticate(email=email, password=password) 
		
		if user:
			login(request, user)
			
			return Response('Loged in!')
		else:
			return Response('User doesn\'t exist', status=404)

class Logout(APIView):

	def get(self, request):
		logout(request)
		return Response('User loged out!')

class Schedule(APIView):

	def get(self, request):
		data = {}
		if request.user.is_authenticated:
			data['pers_workouts'] = Workout.objects.filter(user_id=request.user).order_by('time')



		data['workouts'] = Workout.objects.filter(user=None).order_by('time')
		return Response(data)
