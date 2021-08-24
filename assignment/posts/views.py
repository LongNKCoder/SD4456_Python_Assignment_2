from rest_framework.response import Response
from django.db.models import Q
from rest_framework import viewsets, permissions, generics, status
from knox.auth import TokenAuthentication
from posts.serializers import PostSerializer, CreatePostSerializer
from posts.models import Post
from users.models import Friendship
from assignment.permission import IsOwnerOrReadOnly


class MyPostViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all().filter(owner=user).order_by('-date_post')

class DashboardView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def list(self, request):
        friend_list = [x.friend_id.id for x in Friendship.objects.all().filter(owner_id=request.user.id).only("owner_id")]
        query = Q(owner_id__in=friend_list) & Q(privacy__exact="Pub") | Q(owner_id=request.user.id)
        queryset = Post.objects.all().filter(query).order_by('date_post')
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        self.serializer_class = PostSerializer
        if self.request.GET["user"] != str(self.request.user.id):
            user_id = self.request.GET["user"]
            return Post.objects.all().filter(Q(owner_id=user_id) & Q(privacy="Pub")).order_by('-date_post')
        else:
            return Post.objects.all().filter(owner=self.request.user).order_by('-date_post')

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreatePostSerializer
        request.data["owner"] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
