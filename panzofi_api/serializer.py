from rest_framework import serializers
from panzofi_api.models import Author,Comment,Post,Reply

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = "__all__"
        
class ReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer( read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    
    class Meta:
        model= Reply
        fields = ['id', 'textContent', 'author_id', 'author','created_at','comment']

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, source='reply_set', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    author = AuthorSerializer( read_only=True)
    class Meta:
        model= Comment
        fields = ['id', 'textContent', 'author_id','author','created_at', 'post','replies']
        read_only_fields = ['replies']
        
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    comments = CommentSerializer(many=True, source='comment_set', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'textContent', 'author', 'author_id','created_at', 'comments']
