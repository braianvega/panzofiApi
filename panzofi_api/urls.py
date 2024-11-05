from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, PostViewSet, CommentViewSet, ReplyViewSet

router=routers.DefaultRouter()

router.register(r'author',AuthorViewSet)
router.register(r'post',PostViewSet)
router.register(r'reply',ReplyViewSet)
router.register(r'comment',CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
