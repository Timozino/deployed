from django.urls import path, reverse_lazy, include
from . import views

from django.contrib.auth.views import(PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView)

#app_name='user_app'

urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/update', views.profile_update, name='profile_update'),
    path('login', views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html',success_url=reverse_lazy('registration/password_reset_done.html'), email_template_name='registration/password_reset_confirm.html'), name ='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    
    
]

