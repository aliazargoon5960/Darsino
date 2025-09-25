from django.urls import path
from . import views

app_name = "course_module"
urlpatterns = [
    path('course_list/', views.CourseListView.as_view(), name="course_list"),
    path('detail/<slug:slug>', views.CourseDetailView.as_view(), name="course_detail"),
    path('reg-course/<slug:slug>/', views.RegCourseView.as_view() , name='reg_course'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<slug:slug>', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('search/', views.SearchView.as_view(), name='search_courses'),
]