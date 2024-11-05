from panzofi_api.models import Author, Reply, ReReply, Comment, Post
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import filters
from .serializer import AuthorSerializer, CommentSerializer, ReReplySerializer, ReplySerializer, PostSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = AuthorSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = PostSerializer
    
    @action(detail=True, methods=['get'], url_path='comments')
    def get_comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='all-details')
    def get_all_details(self, request):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)  # Serializamos todos los posts
        return Response(serializer.data)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = CommentSerializer
    
class ReplyViewSet(viewsets.ModelViewSet):
    queryset=Reply.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ReplySerializer
    
class ReReplyViewSet(viewsets.ModelViewSet):
    queryset=ReReply.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ReReplySerializer
    