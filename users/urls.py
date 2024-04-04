from django.urls import path
# from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get_user/', views.get_user),
    path('create_user/', views.create_user),
]

urlpatterns = format_suffix_patterns(urlpatterns)