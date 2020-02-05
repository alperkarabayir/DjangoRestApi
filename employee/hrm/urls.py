from django.urls import path
from . import api

urlpatterns = [
    path('api/users_list/', api.UserList.as_view(), name='user-list'),
    path('api/users_list/<int:employee_id>', api.UserDetail.as_view(), name='user-detail'),
    path('api/auth', api.UserAuthentication.as_view(), name='user-authentication'),
]