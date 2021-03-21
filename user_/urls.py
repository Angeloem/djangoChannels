from django.urls import path

from user_.views import ListCreateUsers, UpdateUsersDelete

urlpatterns = [
    path('', ListCreateUsers.as_view()),
    path('<int:pk>', UpdateUsersDelete.as_view()),
]
