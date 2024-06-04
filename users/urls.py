from django.urls import path
from users.views import *


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/onboarding/', profile_edit_view, name='profile_onboarding'),
    path('profile/settings/', profile_settings_view, name='profile_settings'),
    path('profile/emailchange/', profile_emailchange, name='profile_emailchange'),
    path('profile/emailverify/', profile_emailverify, name='profile_emailverify'),
    path('profile/delete/', profile_delete_view, name='profile_delete'),
]
