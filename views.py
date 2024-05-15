# from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.response import Response    

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "pk"

class MovieOrder(APIView):
    def get(send, request, format=None): 
        ordered_movie = Movie.objects.order_by("title")
        serializer = MovieSerializer(ordered_movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieSearch(APIView):
    def get(send, request, format=None):
        title = request.query_params.get("title", "") 
        if title:
            founded_match = Movie.objects.filter(title__icontains=title)
            serializer = MovieSerializer(founded_match, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)