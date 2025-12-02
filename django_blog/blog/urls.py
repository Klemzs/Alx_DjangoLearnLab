from django.urls import path
from .views import (
    CustomLoginView, 
    CustomLogoutView, 
    register, 
    profile, 
    profile_update, 
    change_password,
    home
)

urlpatterns = [
        # Authenticate URLs 
        path('', home, name='home'),
        path('login/', CustomLoginView.as_view(), name = 'login'),
        path('logout/', CustomLogoutView.as_view(), name = 'logout'),
        path('register/', register, name = 'register'),
        path('profile/', profile, name = 'profile'),

        # Add Profile management URLs
        path('profile/update/', profile_update, name = 'profile_update'),
        path('profile/change-password/', change_password, name = 'change_paswword'),
]
