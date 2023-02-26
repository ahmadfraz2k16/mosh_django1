from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
