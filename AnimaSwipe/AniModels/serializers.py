from rest_framework import serializers
from AniModels.models import User, Pet, GENDER, PET_TYPES
#from multiselectfield import MultiSelectField

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    user_email = serializers.EmailField(max_length=50)
    user_age = serializers.IntegerField(default=0)
    user_password = serializers.CharField(max_length=20)
    user_gender = serializers.MultipleChoiceField(choices=GENDER)
    user_pitch = serializers.CharField(max_length=300)
    
    def create(self, validated_data):
        #Create and return new 'User' instance
        return User.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        #Update and return an existing 'User' instance
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_age = validated_data.get('user_age', instance.user_age)
        instance.user_password = validated_data.get('user_password', instance.user_password)
        instance.user_gender = validated_data.get('user_gender', instance.user_gender)
        instance.user_pitch = validated_data.get('user_pitch', instance.user_pitch)
        instance.save()
        return instance
        
class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pet_name = serializers.CharField(max_length=50)
    pet_type = serializers.MultipleChoiceField(choices=PET_TYPES)
    pet_breed = serializers.CharField(max_length=20)
    pet_age = serializers.IntegerField(default=0)
    pet_gender = serializers.MultipleChoiceField(choices=GENDER)
    pe_description = serializers.CharField(max_length=150)
    user_id = serializers.IntegerField(read_only=True)
    
    def create(self, validated_data):
        #Create and return new 'Pet' instance
        return Pet.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        #Update and return an existing 'Pet' instance
        instance.pet_name = validated_data.get('pet_name', instance.pet_name)
        instance.pet_type = validated_data.get('pet_type', instance.pet_type)
        instance.pet_breed = validated_data.get('pet_breed', instance.pet_breed)
        instance.pet_age = validated_data.get('pet_age', instance.pet_age)
        instance.pet_gender = validated_data.get('pet_gender', instance.pet_gender)
        instance.pet_description = validated_data.get('pet_description', instance.pet_description)
        instance.save()
        return instance