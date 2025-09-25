from django.urls import path
from . import views

app_name = 'user_panel_module'
urlpatterns = [
    path('user-profile/', views.UserProfileView.as_view(), name="user_profile"),
    path('fav-courses', views.FavoriteCourseView.as_view() , name='user_course'),
    path('course/<slug:slug>/delete/', views.DeleteCourseView.as_view(), name='del_course'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit_profile'),
]