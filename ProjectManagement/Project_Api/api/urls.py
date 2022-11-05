from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Registration/',views.UserRegistration.as_view(),name="Registration"),
    path('Project', views.ProjectApi.as_view()),
    path('Project/<str:pk>', views.ProjectApi.as_view()),
     path('Task/', views.TaskApi.as_view()),
     
    # path('Task/gettask/', views.TaskApi.as_view()), custom method url
    path('Permission/', views.PermissionApi.as_view()),
    path('User-Project-Permission/', views.UserProjectPermissionApi.as_view()),
]

