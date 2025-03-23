from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name='Taskease_app-index'),
    path('innerpage', views.innerpage, name='Taskease_app-innerpage'),
    path('portfoliodetails', views.portfoliodetails, name='Taskease_app-portfoliodetails'),
    path('signup-page', views.signuppage, name='Taskease_app-signup-page'),
    path('signin-page', views.signinpage, name='Taskease_app-signin-page'),
    path('signout', views.signout, name='Taskease_app-signout'),
    path('payment-page', views.paymentpage, name='Taskease_app-payment-page'),
    path('profile/', views.profilepage, name='profile'),


]