from django.urls import path
from . import views


app_name = "account_module"
urlpatterns= [
    path('register/' , views.RegisterView.as_view() , name='user_register'),
    path('login/', views.LoginView.as_view(), name="user_login"),
    path('logout/', views.logout_view, name="user_logout"),
]