from panzofi_api.models import Author, Reply, ReReply, Comment, Post
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

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
    
    @action(detail=False, methods=['GET'], url_path='getComments/<int:post_id>')
    def getCommentsByPost(self ,request):
        listComments = self.queryset.filter(post=post_id)
        serializer=self.get_serializer(listComments)
        return Response(serializer.data)
    
class ReplyViewSet(viewsets.ModelViewSet):
    queryset=Reply.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ReplySerializer
    
    @action(detail=False, methods=['GET'], url_path='getReplys/<int:comment_id>')
    def getReplysByComment(self ,request, idComment):
        listReplys = self.queryset.filter(comment=comment_id)
        serializer=self.get_serializer(listReplys)
        return Response(serializer.data)
    
class ReReplyViewSet(viewsets.ModelViewSet):
    queryset=ReReply.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ReReplySerializer
    
    @action(detail=True, methods=['GET'], url_path='getReReplys/<int:replys_id>')
    def getReReplysByReplys(self ,request, idReply):
        listReReplys = self.queryset.filter(reply=Replys_id)
        serializer=self.get_serializer(listReReplys)
        return Response(serializer.data)
