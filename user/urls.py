from django.urls import path,include
from . views import (UserListView,
                    UserDetailView,
                    UserCreateView,
                    UserUpdateView,
                    UserDeleteView,
                    )

app_name = 'user'

urlpatterns = [
    path('api/',include('user.api.urls')),
    path('',UserListView.as_view(),name='list'),
    path('<int:pk>/profile/',UserDetailView.as_view(),name='profile'),
    path('create/',UserCreateView.as_view(),name='create'),
    path('<int:pk>/update/',UserUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',UserDeleteView.as_view(),name='delete'),
]
