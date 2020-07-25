from rest_framework import serializers
from .models import User, Workout
class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        is_staff = validated_data["is_staff"]
        is_superuser = validated_data["is_superuser"]

        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
            {"email": "Email addresses must be unique."})

        user = User(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser', 'password')

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = '__all__'