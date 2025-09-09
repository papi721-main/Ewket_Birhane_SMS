from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView, RoleListCreateView, UserRoleAssignRemoveView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('users/<int:pk>/roles/', UserRoleAssignRemoveView.as_view(), name='user-role-assign'),
    path('users/<int:pk>/roles/<int:role_id>/', UserRoleAssignRemoveView.as_view(), name='user-role-remove'),
]