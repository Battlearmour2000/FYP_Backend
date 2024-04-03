from django.urls import path
# from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('users/', views.UserListCreateAPIView.as_view()),
    # path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('getData/', views.getData),
    path('postData/', views.postData),
]

urlpatterns = format_suffix_patterns(urlpatterns)