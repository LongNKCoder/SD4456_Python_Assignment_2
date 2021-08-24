from rest_framework import routers
from django.urls import re_path
from posts import views

router = routers.DefaultRouter()
router.register('dashboards', views.DashboardView, basename="dashboards")
router.register('posts', views.PostViewSet, basename='posts'),
# router.register('posts', views.CreatePostView, basename='createposts'),
urlpatterns = [
    re_path('myposts', views.MyPostViewSet.as_view(), name='myposts'),
]
urlpatterns += router.urls
