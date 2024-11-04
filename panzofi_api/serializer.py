from rest_framework import serializers
from panzofi_api.models import Author,Comment,Post,Reply, ReReply

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = "__all__"
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = "__all__"
        

class ReReplySerializer(serializers.ModelSerializer):
    class Meta:
        model= ReReply
        fields = "__all__"
        
class ReplySerializer(serializers.ModelSerializer):
    
    rereplies = ReReplySerializer(many=True, source='rereply_set')
    class Meta:
        model= Reply
        fields = ['id', 'textContent', 'author', 'created_at', 'rereplies']
        
class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, source='reply_set')
    class Meta:
        model= Comment
        fields = ['id', 'textContent', 'author', 'created_at', 'replies']