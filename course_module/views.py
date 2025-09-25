from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from . models import Course, Teacher, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class CourseListView(ListView):
    model = Course
    template_name = 'course_module/course_list.html'
    context_object_name = "courses"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context.get('page_obj') 
        if page:
            context['start_index'] = (page.number - 1) * page.paginator.per_page
        else:
            context['start_index'] = 0
        return context


class SearchView(ListView):
    def get(self, request):
        search = request.GET.get('search')
        courses = Course.objects.filter(title__icontains=search)
        return render(request, "course_module/search.html", {'courses' : courses})



class CourseDetailView(DetailView):
    model = Course
    template_name = "course_module/course_detail.html"
    context_object_name = 'course'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')

        parent_comment = None
        if parent_id:
            try:
                parent_comment = Comment.objects.get(id=parent_id, course=course)
            except Comment.DoesNotExist:
                parent_comment = None

        if body:
            Comment.objects.create(course=course, user=request.user, parent=parent_comment, body=body)
        return redirect(course.get_absolute_url())

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        user = self.request.user
        context['is_fav'] = course.fav_students.filter(id=user.id).exists()
        return context



class RegCourseView(LoginRequiredMixin, View):
    def post(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        course.fav_students.add(request.user)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})

        return redirect("course_module:course_detail", slug=slug)


class TeacherListView(ListView):
    model = Teacher
    template_name = "course_module/teacher_list.html"
    context_object_name = "teachers"


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "course_module/teacher_detail.html"
    context_object_name = 'teacher'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(teacher=self.object)
        return context
    




