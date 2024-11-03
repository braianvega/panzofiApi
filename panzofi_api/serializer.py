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
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields = "__all__"

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model= Reply
        fields = "__all__"

class ReReplySerializer(serializers.ModelSerializer):
    class Meta:
        model= ReReply
        fields = "__all__"