from django.http import HttpResponse
from django.views import View
from .serializers import MovieSerializer
from .models import Person, Movie, Role
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)


class MovieView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)