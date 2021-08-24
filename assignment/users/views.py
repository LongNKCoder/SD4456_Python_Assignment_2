from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from users.serializers import CreateUserSerializer, UserSerializer, GroupSerializer, FriendshipSerializer, MakeFriendSerializer
from users.models import Friendship
from assignment.permission import IsOwnerOrReadOnly

# Create your views here.
class UserView(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')


class CreateUserView(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class FriendshipView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        self.serializer_class = FriendshipSerializer
        user_id = self.request.GET["user"]
        return Friendship.objects.all().filter(owner_id=user_id)

    def create(self, request, *args, **kwargs):
        self.serializer_class = MakeFriendSerializer
        owner_id = self.request.user.id
        request.data.update({"owner_id":str(owner_id)})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
