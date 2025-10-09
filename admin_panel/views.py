from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from course_module.models import Course, Teacher, Category
from course_module.forms import CourseForm, TeacherForm, CategoryForm
from blog_module.models import Article, Author
from blog_module.forms import ArticleForm, AuthorForm
from contact_module.models import Message
from tickets_module.models import Ticket, TicketAttachment, TicketReply
from tickets_module.forms import TicketCreateForm, TicketReplyForm
from site_module.models import SiteSetting, FooterLinkBox, FooterLink, Banner
from site_module.forms import SiteSettingForm, FooterLinkBoxForm, FooterLinkForm, BannerForm
from cart_module.models import Order, DiscountCode
from cart_module.forms import DiscountCodeForm
from account_module.models import User
from account_module.forms import UserForm


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# ===== Dashboard =====
class DashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'admin_panel/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_courses'] = Course.objects.count()
        context['total_articles'] = Article.objects.count()
        context['unread_messages'] = Message.objects.count()
        context['open_tickets'] = Ticket.objects.filter(status='open').count()
        return context


# ===== Users  =====

class UserListView(ListView):
    model = User
    template_name = 'admin_panel/user/user_list.html'
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'admin_panel/user/user_form.html'
    success_url = reverse_lazy('admin_panel:user_list')

    def form_valid(self, form):
        messages.success(self.request, "کاربر با موفقیت اضافه شد.")
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'admin_panel/user/user_form.html'
    success_url = reverse_lazy('admin_panel:user_list')

    def form_valid(self, form):
        messages.success(self.request, "اطلاعات کاربر بروزرسانی شد.")
        self.object = form.save(commit=False)
        self.object.save()
        form.save()
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admin_panel/user/user_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:user_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "کاربر حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Course =====
class CourseListView(StaffRequiredMixin, ListView):
    model = Course
    template_name = 'admin_panel/course/course_list.html'
    context_object_name = 'courses'
    ordering = ['-created']

class CourseCreateView(StaffRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin_panel/course/course_form.html'
    success_url = reverse_lazy('admin_panel:course_list')

    def form_valid(self, form):
        messages.success(self.request, "دوره با موفقیت اضافه شد.")
        return super().form_valid(form)

class CourseUpdateView(StaffRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'admin_panel/course/course_form.html'
    success_url = reverse_lazy('admin_panel:course_list')

    def form_valid(self, form):
        messages.success(self.request, "دوره با موفقیت بروزرسانی شد.")
        return super().form_valid(form)

class CourseDeleteView(StaffRequiredMixin, DeleteView):
    model = Course
    template_name = 'admin_panel/course/course_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:course_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "دوره با موفقیت حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Teacher =====
class TeacherListView(StaffRequiredMixin, ListView):
    model = Teacher
    template_name = 'admin_panel/teacher/teacher_list.html'
    context_object_name = 'teachers'

class TeacherCreateView(StaffRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'admin_panel/teacher/teacher_form.html'
    success_url = reverse_lazy('admin_panel:teacher_list')

    def form_valid(self, form):
        messages.success(self.request, "مدرس جدید اضافه شد.")
        return super().form_valid(form)

class TeacherUpdateView(StaffRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'admin_panel/teacher/teacher_form.html'
    success_url = reverse_lazy('admin_panel:teacher_list')

    def form_valid(self, form):
        messages.success(self.request, "اطلاعات مدرس بروزرسانی شد.")
        return super().form_valid(form)

class TeacherDeleteView(StaffRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'admin_panel/teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:teacher_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "مدرس حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Category =====
class CategoryListView(StaffRequiredMixin, ListView):
    model = Category
    template_name = 'admin_panel/course/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_panel/course/category_form.html'
    success_url = reverse_lazy('admin_panel:category_list')

    def form_valid(self, form):
        messages.success(self.request, "دسته بندی جدید اضافه شد.")
        return super().form_valid(form)

class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_panel/course/category_form.html'
    success_url = reverse_lazy('admin_panel:category_list')

    def form_valid(self, form):
        messages.success(self.request, "دسته بندی بروزرسانی شد.")
        return super().form_valid(form)

class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    model = Category
    template_name = 'admin_panel/course/category_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "دسته بندی حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Article =====
class ArticleListView(StaffRequiredMixin, ListView):
    model = Article
    template_name = 'admin_panel/article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

class ArticleCreateView(StaffRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin_panel/article/article_form.html'
    success_url = reverse_lazy('admin_panel:article_list')

    def form_valid(self, form):
        messages.success(self.request, "مقاله با موفقیت اضافه شد.")
        return super().form_valid(form)

class ArticleUpdateView(StaffRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin_panel/article/article_form.html'
    success_url = reverse_lazy('admin_panel:article_list')

    def form_valid(self, form):
        messages.success(self.request, "مقاله با موفقیت بروزرسانی شد.")
        return super().form_valid(form)

class ArticleDeleteView(StaffRequiredMixin, DeleteView):
    model = Article
    template_name = 'admin_panel/article/article_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:article_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "مقاله با موفقیت حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Author =====
class AuthorListView(StaffRequiredMixin, ListView):
    model = Author
    template_name = 'admin_panel/article/author_list.html'
    context_object_name = 'authors'

class AuthorCreateView(StaffRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'admin_panel/article/author_form.html'
    success_url = reverse_lazy('admin_panel:author_list')

    def form_valid(self, form):
        messages.success(self.request, "نویسنده با موفقیت اضافه شد.")
        return super().form_valid(form)

class AuthorUpdateView(StaffRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'admin_panel/article/author_form.html'
    success_url = reverse_lazy('admin_panel:author_list')

    def form_valid(self, form):
        messages.success(self.request, "نویسنده بروزرسانی شد.")
        return super().form_valid(form)

class AuthorDeleteView(StaffRequiredMixin, DeleteView):
    model = Author
    template_name = 'admin_panel/article/author_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:author_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "نویسنده حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Message =====
class ContactListView(StaffRequiredMixin, ListView):
    model = Message
    template_name = 'admin_panel/contact/contact_list.html'
    context_object_name = 'messages'
    ordering = ['-created_at']

class ContactDetailView(StaffRequiredMixin, DetailView):
    model = Message
    template_name = 'admin_panel/contact/contact_detail.html'
    context_object_name = 'message'

# ===== Ticket =====
class TicketListView(StaffRequiredMixin, ListView):
    model = Ticket
    template_name = 'admin_panel/tickets/ticket_list.html'
    context_object_name = 'tickets'
    ordering = ['-created_at']

class TicketDetailView(StaffRequiredMixin, DetailView):
    model = Ticket
    template_name = 'admin_panel/tickets/ticket_detail.html'
    context_object_name = 'ticket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TicketReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        form = TicketReplyForm(request.POST)
        files = request.FILES.getlist('files')
        if form.is_valid():
            form.save(reply_user=request.user, ticket=ticket, files=files)
            messages.success(request, "پاسخ با موفقیت ارسال شد.")
            return redirect('admin_panel:ticket_detail', pk=ticket.pk)
        return self.get(request, *args, **kwargs)

# ===== Site Setting =====
class SiteSettingListView(StaffRequiredMixin, ListView):
    model = SiteSetting
    template_name = 'admin_panel/site/site_setting_list.html'
    context_object_name = 'settings'

class SiteSettingCreateView(StaffRequiredMixin, CreateView):
    model = SiteSetting
    form_class = SiteSettingForm
    template_name = 'admin_panel/site/site_setting_form.html'
    success_url = reverse_lazy('admin_panel:site_setting_list')

    def form_valid(self, form):
        messages.success(self.request, "تنظیمات سایت با موفقیت اضافه شد.")
        return super().form_valid(form)

class SiteSettingUpdateView(StaffRequiredMixin, UpdateView):
    model = SiteSetting
    form_class = SiteSettingForm
    template_name = 'admin_panel/site/site_setting_form.html'
    success_url = reverse_lazy('admin_panel:site_setting_list')

    def form_valid(self, form):
        messages.success(self.request, "تنظیمات سایت با موفقیت بروزرسانی شد.")
        return super().form_valid(form)

# ===== FooterLinkBox =====
class FooterBoxListView(StaffRequiredMixin, ListView):
    model = FooterLinkBox
    template_name = 'admin_panel/site/footer_box_list.html'
    context_object_name = 'boxes'

class FooterBoxCreateView(StaffRequiredMixin, CreateView):
    model = FooterLinkBox
    form_class = FooterLinkBoxForm
    template_name = 'admin_panel/site/footer_box_form.html'
    success_url = reverse_lazy('admin_panel:footer_box_list')

    def form_valid(self, form):
        messages.success(self.request, "دسته بندی لینک فوتر اضافه شد.")
        return super().form_valid(form)

class FooterBoxUpdateView(StaffRequiredMixin, UpdateView):
    model = FooterLinkBox
    form_class = FooterLinkBoxForm
    template_name = 'admin_panel/site/footer_box_form.html'
    success_url = reverse_lazy('admin_panel:footer_box_list')

    def form_valid(self, form):
        messages.success(self.request, "دسته بندی لینک فوتر بروزرسانی شد.")
        return super().form_valid(form)

class FooterBoxDeleteView(StaffRequiredMixin, DeleteView):
    model = FooterLinkBox
    template_name = 'admin_panel/site/footer_box_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:footer_box_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "دسته بندی لینک فوتر حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== FooterLink =====
class FooterLinkListView(StaffRequiredMixin, ListView):
    model = FooterLink
    template_name = 'admin_panel/site/footer_link_list.html'
    context_object_name = 'links'

class FooterLinkCreateView(StaffRequiredMixin, CreateView):
    model = FooterLink
    form_class = FooterLinkForm
    template_name = 'admin_panel/site/footer_link_form.html'
    success_url = reverse_lazy('admin_panel:footer_link_list')

    def form_valid(self, form):
        messages.success(self.request, "لینک فوتر اضافه شد.")
        return super().form_valid(form)

class FooterLinkUpdateView(StaffRequiredMixin, UpdateView):
    model = FooterLink
    form_class = FooterLinkForm
    template_name = 'admin_panel/site/footer_link_form.html'
    success_url = reverse_lazy('admin_panel:footer_link_list')

    def form_valid(self, form):
        messages.success(self.request, "لینک فوتر بروزرسانی شد.")
        return super().form_valid(form)

class FooterLinkDeleteView(StaffRequiredMixin, DeleteView):
    model = FooterLink
    template_name = 'admin_panel/site/footer_link_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:footer_link_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "لینک فوتر حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Banner =====
class BannerListView(StaffRequiredMixin, ListView):
    model = Banner
    template_name = 'admin_panel/site/banner_list.html'
    context_object_name = 'banners'

class BannerCreateView(StaffRequiredMixin, CreateView):
    model = Banner
    form_class = BannerForm
    template_name = 'admin_panel/site/banner_form.html'
    success_url = reverse_lazy('admin_panel:banner_list')

    def form_valid(self, form):
        messages.success(self.request, "بنر اضافه شد.")
        return super().form_valid(form)

class BannerUpdateView(StaffRequiredMixin, UpdateView):
    model = Banner
    form_class = BannerForm
    template_name = 'admin_panel/site/banner_form.html'
    success_url = reverse_lazy('admin_panel:banner_list')

    def form_valid(self, form):
        messages.success(self.request, "بنر بروزرسانی شد.")
        return super().form_valid(form)

class BannerDeleteView(StaffRequiredMixin, DeleteView):
    model = Banner
    template_name = 'admin_panel/site/banner_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:banner_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "بنر حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== DiscountCode =====
class DiscountListView(StaffRequiredMixin, ListView):
    model = DiscountCode
    template_name = 'admin_panel/cart/discount_list.html'
    context_object_name = 'codes'

class DiscountCreateView(StaffRequiredMixin, CreateView):
    model = DiscountCode
    form_class = DiscountCodeForm
    template_name = 'admin_panel/cart/discount_form.html'
    success_url = reverse_lazy('admin_panel:discount_list')

    def form_valid(self, form):
        messages.success(self.request, "کد تخفیف اضافه شد.")
        return super().form_valid(form)

class DiscountUpdateView(StaffRequiredMixin, UpdateView):
    model = DiscountCode
    form_class = DiscountCodeForm
    template_name = 'admin_panel/cart/discount_form.html'
    success_url = reverse_lazy('admin_panel:discount_list')

    def form_valid(self, form):
        messages.success(self.request, "کد تخفیف بروزرسانی شد.")
        return super().form_valid(form)

class DiscountDeleteView(StaffRequiredMixin, DeleteView):
    model = DiscountCode
    template_name = 'admin_panel/cart/discount_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:discount_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "کد تخفیف حذف شد.")
        return super().delete(request, *args, **kwargs)

# ===== Order =====
class OrderListView(StaffRequiredMixin, ListView):
    model = Order
    template_name = 'admin_panel/cart/order_list.html'
    context_object_name = 'orders'
    ordering = ['-id']

class OrderDetailView(StaffRequiredMixin, DetailView):
    model = Order
    template_name = 'admin_panel/cart/order_detail.html'
    context_object_name = 'order'
