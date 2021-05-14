from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from .views import Login, UserList, UserDetail, UserUpdate, PasswordChange

app_name = 'web'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/password_change/', PasswordChange.as_view(), name='password-change'),

    path('', Login.as_view(), name='login'),
    path('guest/', views.register_guest, name='registerGuest'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

    path('register/user/', views.register_user, name='registerUser'),
    path('view/user/', login_required(UserList.as_view(), login_url='/'),
         name='userList'),
    path('view/user/<int:pk>', login_required(UserDetail.as_view(), login_url='/'),
         name='userDetail'),
    path('view/user/<int:pk>/update/', login_required(UserUpdate.as_view(), login_url='/'),
         name='userUpdate'),
    path('delete-user/', views.delete_user, name='deleteUser'),
]
