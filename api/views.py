from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostList(APIView):
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True, context={'request': request})
        return Response(serializer.data)
        
