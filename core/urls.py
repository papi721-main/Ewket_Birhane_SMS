#!/usr/bin/env python3
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView, RoleListCreateView, UserRoleAssignRemoveView, BatchListCreateView, BatchRetrieveUpdateDeleteView, DepartmentListCreateView, DepartmentRetrieveUpdateDeleteView, SubjectListCreateView, SubjectRetrieveUpdateDeleteView, UserRetrieveByUsernameView, UserManageByUsernameView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('users/<int:pk>/roles/', UserRoleAssignRemoveView.as_view(), name='user-role-assign'),
    path('users/<int:pk>/roles/<int:role_id>/', UserRoleAssignRemoveView.as_view(), name='user-role-remove'),
    path('batches/', BatchListCreateView.as_view(), name='batch-list-create'),
    path('batches/<int:pk>/', BatchRetrieveUpdateDeleteView.as_view(), name='batch-retrieve-update-delete'),
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDeleteView.as_view(), name='department-retrieve-update-delete'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDeleteView.as_view(), name='subject-retrieve-update-delete'),
    path('users/username/<str:username>/', UserRetrieveByUsernameView.as_view(), name='user-retrieve-by-username'),
    path('users/username/<str:username>/', UserManageByUsernameView.as_view(), name='user-manage-by-username'),
]
