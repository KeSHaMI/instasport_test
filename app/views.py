from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView


from api.models import User, Workout
from api.serializers import UserSerializer, WorkoutSerializer
# Create your views here.

class Register(APIView):

	def get(self, request):
		return render(request, 'app/register.html')

	def post(self, request):

		serializer = UserSerializer(data=request.data) 
		
		if serializer.is_valid():
			serializer.save()
			
			return redirect('/')
		else:
			return Response(serializer.errors, status=400)

class Login(APIView):

	def get(self, request):
		return render(request, 'app/login.html')


	def post(self, request):

		email = request.data.get('email')
		password = request.data.get('password')

		user = authenticate(email=email, password=password) 
		
		if user:
			login(request, user)
			
			return redirect('/')
		else:
			return Response('User doesn\'t exist', status=404)

class Logout(APIView):

	def get(self, request):
		logout(request)
		return redirect('/')

class Schedule(APIView):

	def get(self, request):
		context = {}
		if request.user.is_authenticated:
			context['authenticated'] = True
			context['pers_workouts'] = Workout.objects.filter(user_id=request.user).order_by('time')



		context['workouts'] = Workout.objects.filter(user=None).order_by('time')
		print(context)
		return render(request, 'app/schedule.html', context)
