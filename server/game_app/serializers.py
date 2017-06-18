
from rest_framework import serializers
from game_app.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','password')
