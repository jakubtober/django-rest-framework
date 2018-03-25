from rest_framework import serializers
from .models import Movie, Person, Role


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'last_name']




class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')

    class Meta:
        model = Role
        fields = ['id', 'name', 'role']


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    actors = RoleSerializer(many=True, source='role_set')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'director', 'actors']
