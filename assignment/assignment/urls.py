"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns as user_router
from posts.urls import urlpatterns as post_router
from users.views import LoginView, CreateUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_router)),
    path('', include(post_router)),
    path('login/', LoginView.as_view()),
    path('register/', CreateUserView.as_view()),
]
