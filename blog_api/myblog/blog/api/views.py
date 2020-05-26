from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from blog.models import post
from .serializers import PostListSerializer, PostCreateSerializer, PostUpdateSerializer, PostDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,  #superuser
                                        IsAuthenticatedOrReadOnly)
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import (SearchFilter, OrderingFilter)
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

class PostListAPIView(ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title', 'content','user__username']
    pagination_class = PostLimitOffsetPagination #عدد الصفحات المتاحة
    # pagination_class = PostPageNumberPagination #رقم الصفحة التالية


class PostCreateAPIView(CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'  #لو معملتش دا , لازم اكتب pk بدل id في url
    def delete(self, request, id):
        queryset = get_object_or_404(post, id=id)
        queryset.delete()


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class PostDeleteAPIView(DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]