
from django.urls import path
from . import views


urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('users', UserList.as_view(), name='userList'),
    path('users/<int:id>', UserDetail.as_view(), name='userDetail'),
]
