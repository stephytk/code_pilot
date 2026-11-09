from rest_framework import serializers

from account.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","password","email","phone","role"]

        read_only_fields =["id","role"]

class StudentSerilaizer(serializers.ModelSerializer):


    class Meta:
   

        model = User

        fields =["__all__"]

        read_only_fields =["id","student","created_at","updated_at"]

