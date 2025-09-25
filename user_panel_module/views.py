from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from course_module.models import Course
from . forms import UserProfileForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_panel_module/user_profile_page.html'



class FavoriteCourseView(LoginRequiredMixin,ListView):
    template_name = "user_panel_module/favorite_courses.html"
    context_object_name = "course"
    def get_queryset(self):
        return self.request.user.fav_courses.all()


class DeleteCourseView(View):
    def post(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        course.fav_students.remove(request.user)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})

        messages.success(request, 'شما از دوره خارج شدید.')
        return redirect("user_panel_module:user_course")
    
    

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile_form = UserProfileForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
        return render(request,"user_panel_module/edit_profile.html", {'form': profile_form,'password_form': password_form })

    def post(self, request):
        if "profile_submit" in request.POST:
            profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user)
            
            if profile_form.is_valid():
                user = profile_form.save(commit=False)
                user.username = user.email 
                user.save()
                messages.success(request, "تغییرات پروفایل با موفقیت ذخیره شد.")
                return redirect("user_panel_module:edit_profile")

        elif "password_submit" in request.POST:
            profile_form = UserProfileForm(instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  
                messages.success(request, "رمز عبور شما با موفقیت تغییر کرد.")
                return redirect("user_panel_module:edit_profile")

        
        return render(request, "user_panel_module/edit_profile.html", {'form': profile_form,'password_form': password_form})

