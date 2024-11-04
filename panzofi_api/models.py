from django.db import models
# Create your models here.

class Author(models.Model):
    username=models.TextField(unique=True)
    name=models.TextField()
    userUrlImage=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    
class Post(models.Model):
    textContent=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    
class Comment(models.Model):
    textContent=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Reply(models.Model):
    textContent=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class ReReply(models.Model):
    textContent=models.TextField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    reply=models.ForeignKey(Reply, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)