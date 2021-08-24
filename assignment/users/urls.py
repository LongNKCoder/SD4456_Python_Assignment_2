from django.urls import re_path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register('groups', views.GroupViewSet)
router.register('friends', views.FriendshipView, basename='friends'),
urlpatterns = [
    re_path('users', views.UserView.as_view(), name='users'),
]
urlpatterns += router.urls
