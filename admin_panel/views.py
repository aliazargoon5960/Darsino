from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from course_module.models import Course, Teacher, Category
from blog_module.models import Article, Author
from contact_module.models import Message
from tickets_module.models import Ticket, TicketAttachment, TicketReply
from django.contrib import messages
from course_module.forms import CourseForm , TeacherForm, CategoryForm
from blog_module.forms import ArticleForm, AuthorForm
from django.contrib.auth.decorators import login_required
from tickets_module.forms import TicketCreateForm, TicketReplyForm
from site_module.models import SiteSetting, FooterLinkBox, FooterLink, Banner
from site_module.forms import SiteSettingForm, FooterLinkBoxForm, FooterLinkForm, BannerForm
from cart_module.models import Order,DiscountCode
from cart_module.forms import DiscountCodeForm


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

# teacher
@staff_member_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'admin_panel/teacher/teacher_list.html', {'teachers': teachers})

@staff_member_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "مدرس جدید اضافه شد.")
            return redirect('admin_panel:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'admin_panel/teacher/teacher_form.html', {'form': form})

@staff_member_required
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "اطلاعات مدرس بروزرسانی شد.")
            return redirect('admin_panel:teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'admin_panel/teacher/teacher_form.html', {'form': form, 'teacher': teacher})

@staff_member_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, "مدرس حذف شد.")
        return redirect('admin_panel:teacher_list')
    return render(request, 'admin_panel/teacher/teacher_confirm_delete.html', {'teacher': teacher})

# Category
@staff_member_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'admin_panel/course/category_list.html', {'categories': categories})

@staff_member_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "دسته بندی جدید اضافه شد.")
            return redirect('admin_panel:category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin_panel/course/category_form.html', {'form': form})

@staff_member_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "دسته بندی بروزرسانی شد.")
            return redirect('admin_panel:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin_panel/course/category_form.html', {'form': form, 'category': category})

@staff_member_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "دسته بندی حذف شد.")
        return redirect('admin_panel:category_list')
    return render(request, 'admin_panel/course/category_confirm_delete.html', {'category': category})



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

# author

@staff_member_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'admin_panel/article/author_list.html', {'authors': authors})


@staff_member_required
def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "نویسنده با موفقیت اضافه شد.")
            return redirect('admin_panel:author_list')
    else:
        form = AuthorForm()
    return render(request, 'admin_panel/article/author_form.html', {'form': form})

@staff_member_required
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "نویسنده بروزرسانی شد.")
            return redirect('admin_panel:author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'admin_panel/article/author_form.html', {'form': form, 'author': author})

@staff_member_required
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        messages.success(request, "نویسنده حذف شد.")
        return redirect('admin_panel:author_list')
    return render(request, 'admin_panel/article/author_confirm_delete.html', {'author': author})


#message
@staff_member_required
def contact_list(request):
    messages_list = Message.objects.all().order_by('-created_at')  
    return render(request, 'admin_panel/contact/contact_list.html', {'messages': messages_list})

@staff_member_required
def contact_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)

    
    return render(request, 'admin_panel/contact/contact_detail.html', {'message': message})


#ticket
@staff_member_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/tickets/ticket_list.html', {'tickets': tickets})


@staff_member_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == "POST":
        form = TicketReplyForm(request.POST)
        files = request.FILES.getlist('files')
        if form.is_valid():
            form.save(reply_user=request.user, ticket=ticket, files=files)
            messages.success(request, "پاسخ با موفقیت ارسال شد.")
            return redirect('admin_panel:ticket_detail', pk=ticket.pk)
    else:
        form = TicketReplyForm()

    return render(request, 'admin_panel/tickets/ticket_detail.html', {
        'ticket': ticket,
        'form': form,
    })

# site setting
@staff_member_required
def site_setting_list(request):
    settings = SiteSetting.objects.all()
    return render(request, 'admin_panel/site/site_setting_list.html', {'settings': settings})


@staff_member_required
def site_setting_create(request):
    if request.method == 'POST':
        form = SiteSettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تنظیمات سایت با موفقیت اضافه شد.")
            return redirect('admin_panel:site_setting_list')
    else:
        form = SiteSettingForm()
    return render(request, 'admin_panel/site/site_setting_form.html', {'form': form, 'setting': None})


@staff_member_required
def site_setting_update(request, pk):
    setting = get_object_or_404(SiteSetting, pk=pk)
    if request.method == 'POST':
        form = SiteSettingForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, "تنظیمات سایت با موفقیت بروزرسانی شد.")
            return redirect('admin_panel:site_setting_list')
    else:
        form = SiteSettingForm(instance=setting)
    return render(request, 'admin_panel/site/site_setting_form.html', {'form': form, 'setting': setting})

# ====== FooterLinkBox ======
@staff_member_required
def footer_box_list(request):
    boxes = FooterLinkBox.objects.all()
    return render(request, 'admin_panel/site/footer_box_list.html', {'boxes': boxes})

@staff_member_required
def footer_box_create(request):
    if request.method == 'POST':
        form = FooterLinkBoxForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "دسته بندی لینک فوتر اضافه شد.")
            return redirect('admin_panel:footer_box_list')
    else:
        form = FooterLinkBoxForm()
    return render(request, 'admin_panel/site/footer_box_form.html', {'form': form})

@staff_member_required
def footer_box_update(request, pk):
    box = get_object_or_404(FooterLinkBox, pk=pk)
    if request.method == 'POST':
        form = FooterLinkBoxForm(request.POST, instance=box)
        if form.is_valid():
            form.save()
            messages.success(request, "دسته بندی لینک فوتر بروزرسانی شد.")
            return redirect('admin_panel:footer_box_list')
    else:
        form = FooterLinkBoxForm(instance=box)
    return render(request, 'admin_panel/site/footer_box_form.html', {'form': form, 'box': box})

@staff_member_required
def footer_box_delete(request, pk):
    box = get_object_or_404(FooterLinkBox, pk=pk)
    if request.method == 'POST':
        box.delete()
        messages.success(request, "دسته بندی لینک فوتر حذف شد.")
        return redirect('admin_panel:footer_box_list')
    return render(request, 'admin_panel/site/footer_box_confirm_delete.html', {'box': box})

# ====== FooterLink ======
@staff_member_required
def footer_link_list(request):
    links = FooterLink.objects.all()
    return render(request, 'admin_panel/site/footer_link_list.html', {'links': links})

@staff_member_required
def footer_link_create(request):
    if request.method == 'POST':
        form = FooterLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "لینک فوتر اضافه شد.")
            return redirect('admin_panel:footer_link_list')
    else:
        form = FooterLinkForm()
    return render(request, 'admin_panel/site/footer_link_form.html', {'form': form})

@staff_member_required
def footer_link_update(request, pk):
    link = get_object_or_404(FooterLink, pk=pk)
    if request.method == 'POST':
        form = FooterLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, "لینک فوتر بروزرسانی شد.")
            return redirect('admin_panel:footer_link_list')
    else:
        form = FooterLinkForm(instance=link)
    return render(request, 'admin_panel/site/footer_link_form.html', {'form': form, 'link': link})

@staff_member_required
def footer_link_delete(request, pk):
    link = get_object_or_404(FooterLink, pk=pk)
    if request.method == 'POST':
        link.delete()
        messages.success(request, "لینک فوتر حذف شد.")
        return redirect('admin_panel:footer_link_list')
    return render(request, 'admin_panel/site/footer_link_confirm_delete.html', {'link': link})

# ====== Banner ======
@staff_member_required
def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'admin_panel/site/banner_list.html', {'banners': banners})

@staff_member_required
def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "بنر اضافه شد.")
            return redirect('admin_panel:banner_list')
    else:
        form = BannerForm()
    return render(request, 'admin_panel/site/banner_form.html', {'form': form})

@staff_member_required
def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, "بنر بروزرسانی شد.")
            return redirect('admin_panel:banner_list')
    else:
        form = BannerForm(instance=banner)
    return render(request, 'admin_panel/site/banner_form.html', {'form': form, 'banner': banner})

@staff_member_required
def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        messages.success(request, "بنر حذف شد.")
        return redirect('admin_panel:banner_list')
    return render(request, 'admin_panel/site/banner_confirm_delete.html', {'banner': banner})


# ====== DiscountCode ======
@staff_member_required
def discount_list(request):
    codes = DiscountCode.objects.all()
    return render(request, 'admin_panel/cart/discount_list.html', {'codes': codes})

@staff_member_required
def discount_create(request):
    if request.method == 'POST':
        form = DiscountCodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "کد تخفیف اضافه شد.")
            return redirect('admin_panel:discount_list')
    else:
        form = DiscountCodeForm()
    return render(request, 'admin_panel/cart/discount_form.html', {'form': form})

@staff_member_required
def discount_update(request, pk):
    code = get_object_or_404(DiscountCode, pk=pk)
    if request.method == 'POST':
        form = DiscountCodeForm(request.POST, instance=code)
        if form.is_valid():
            form.save()
            messages.success(request, "کد تخفیف بروزرسانی شد.")
            return redirect('admin_panel:discount_list')
    else:
        form = DiscountCodeForm(instance=code)
    return render(request, 'admin_panel/cart/discount_form.html', {'form': form, 'code': code})

@staff_member_required
def discount_delete(request, pk):
    code = get_object_or_404(DiscountCode, pk=pk)
    if request.method == 'POST':
        code.delete()
        messages.success(request, "کد تخفیف حذف شد.")
        return redirect('admin_panel:discount_list')
    return render(request, 'admin_panel/cart/discount_confirm_delete.html', {'code': code})

# ====== Orders ======
@staff_member_required
def order_list(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'admin_panel/cart/order_list.html', {'orders': orders})

@staff_member_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'admin_panel/cart/order_detail.html', {'order': order})