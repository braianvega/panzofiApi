from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Comment, Reply, ReReply, Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(ReReply)
