from django.shortcuts import get_object_or_404
from blog.models import Post
from blog.serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_post = Post.objects.all()
    data = PostSerializers(all_post,many=True,context={'request':request}).data
    return Response({'data':data})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request,id):
    post =  get_object_or_404(Post,id=id)
    data = PostSerializers(post).data
    return Response({'data':data})
    
@api_view(['GET'])  
@permission_classes([IsAuthenticated])
def create_search_api(request,query):
    posts = Post.objects.filter(
        Q(title__icontains= query) | 
        Q(description__icontains = query)
    )
    data = PostSerializers(posts,many=True).data
    return Response({'data':data})