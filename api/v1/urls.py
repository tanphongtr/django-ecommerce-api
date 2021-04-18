"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .auth import AuthViewSet, UserSignUpViewSet, AuthLogoutViewSet, AuthForgotPasswordViewSet
from .post import PostViewSet, PostDetailViewSet, PostExportViewSet
from .file import FileAPIView, FileDetailAPIView

urlpatterns = [
    path('auth/login/', AuthViewSet.as_view()),
    path('auth/signup/', UserSignUpViewSet.as_view()),
    path('auth/logout/', AuthLogoutViewSet.as_view()),
    path('auth/forgotpassword/', AuthForgotPasswordViewSet.as_view()),
    path('posts/', PostViewSet.as_view()),
    path('posts/<uuid:sid>/', PostDetailViewSet.as_view()),
    path('posts/export/', PostExportViewSet.as_view({'get': 'list'})),


    path('files/', FileAPIView.as_view()),
    path('files/<uuid:sid>/', FileDetailAPIView.as_view()),
    # path('test/', Test.as_view()),
] 
