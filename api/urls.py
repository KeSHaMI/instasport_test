from django.urls import path
from .views import Register, Login, Logout, Schedule

urlpatterns = [
	path('register/', Register.as_view()),
	path('login/', Login.as_view()),
	path('logout/', Logout.as_view()),
	path('schedule/', Schedule.as_view())
]
