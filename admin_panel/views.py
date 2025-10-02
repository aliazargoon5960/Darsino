from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from course_module.models import Course
from blog_module.models import Article
from contact_module.models import Message
from tickets_module.models import Ticket, TicketAttachment
from django.contrib import messages
from course_module.forms import CourseForm 
from blog_module.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from tickets_module.forms import TicketCreateForm, TicketReplyForm

@staff_member_required
def index(request):
    total_courses = Course.objects.count()
    total_articles = Article.objects.count()
    unread_messages = Message.objects.all().count()
    open_tickets = Ticket.objects.filter(status='open').count()
    
    context = {
        'total_courses': total_courses,
        'total_articles': total_articles,
        'unread_messages': unread_messages,
        'open_tickets': open_tickets,
    }
    return render(request, 'admin_panel/index.html', context)


#course
@staff_member_required
def course_list(request):
    courses = Course.objects.all().order_by('-created')
    return render(request, 'admin_panel/course/course_list.html', {'courses': courses})

@staff_member_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "دوره با موفقیت اضافه شد.")
            return redirect('admin_panel:course_list')
    else:
        form = CourseForm()
    return render(request, 'admin_panel/course/course_form.html', {'form': form})



@staff_member_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "دوره با موفقیت بروزرسانی شد.")
            return redirect('admin_panel:course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'admin_panel/course/course_form.html', {'form': form, 'course': course})

@staff_member_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "دوره با موفقیت حذف شد.")
        return redirect('admin_panel:course_list')
    return render(request, 'admin_panel/course/course_confirm_delete.html', {'course': course})



#article
@staff_member_required
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/article/article_list.html', {'articles': articles})

@staff_member_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "مقاله با موفقیت اضافه شد.")
            return redirect('admin_panel:article_list')
    else:
        form = ArticleForm()
    return render(request, 'admin_panel/article/article_form.html', {'form': form})

@staff_member_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "مقاله با موفقیت بروزرسانی شد.")
            return redirect('admin_panel:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'admin_panel/article/article_form.html', {'form': form, 'article': article})

@staff_member_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "مقاله با موفقیت حذف شد.")
        return redirect('admin_panel:article_list')
    return render(request, 'admin_panel/article/article_confirm_delete.html', {'article': article})

#message
@staff_member_required
def contact_list(request):
    messages_list = Message.objects.all().order_by('-created_at')  
    return render(request, 'admin_panel/contact/contact_list.html', {'messages': messages_list})

@staff_member_required
def contact_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)

    
    return render(request, 'admin_panel/contact/contact_detail.html', {'message': message})

