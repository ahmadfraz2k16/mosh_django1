from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['size', 'name', 'phone_number', 'cnic']
        fields = ['image', 'size', 'name', 'phone_number', 'cnic']
