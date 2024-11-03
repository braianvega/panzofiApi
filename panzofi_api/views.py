from panzofi_api.models import Author, Reply, ReReply, Comment, Post
from rest_framework import viewsets, permissions
from .serializer import AuthorSerializer, CommentSerializer, ReReplySerializer, ReplySerializer, PostSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = AuthorSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = PostSerializer
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