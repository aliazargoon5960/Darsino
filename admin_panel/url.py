from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),

    # Users
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),

    # Courses
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Teachers
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),

    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Articles
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

    # Authors
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),

    # Messages
    path('contacts/', views.ContactListView.as_view(), name='contact_list'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),

    # Tickets
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),

    # Site Settings
    path('site-settings/', views.SiteSettingListView.as_view(), name='site_setting_list'),
    path('site-settings/create/', views.SiteSettingCreateView.as_view(), name='site_setting_create'),
    path('site-settings/update/<int:pk>/', views.SiteSettingUpdateView.as_view(), name='site_setting_update'),

    # Footer Boxes
    path('footer-boxes/', views.FooterBoxListView.as_view(), name='footer_box_list'),
    path('footer-boxes/create/', views.FooterBoxCreateView.as_view(), name='footer_box_create'),
    path('footer-boxes/update/<int:pk>/', views.FooterBoxUpdateView.as_view(), name='footer_box_update'),
    path('footer-boxes/delete/<int:pk>/', views.FooterBoxDeleteView.as_view(), name='footer_box_delete'),

    # Footer Links
    path('footer-links/', views.FooterLinkListView.as_view(), name='footer_link_list'),
    path('footer-links/create/', views.FooterLinkCreateView.as_view(), name='footer_link_create'),
    path('footer-links/update/<int:pk>/', views.FooterLinkUpdateView.as_view(), name='footer_link_update'),
    path('footer-links/delete/<int:pk>/', views.FooterLinkDeleteView.as_view(), name='footer_link_delete'),

    # Banners
    path('banners/', views.BannerListView.as_view(), name='banner_list'),
    path('banners/create/', views.BannerCreateView.as_view(), name='banner_create'),
    path('banners/update/<int:pk>/', views.BannerUpdateView.as_view(), name='banner_update'),
    path('banners/delete/<int:pk>/', views.BannerDeleteView.as_view(), name='banner_delete'),

    # Discount Codes
    path('discount/', views.DiscountListView.as_view(), name='discount_list'),
    path('discount/add/', views.DiscountCreateView.as_view(), name='discount_create'),
    path('discount/<int:pk>/edit/', views.DiscountUpdateView.as_view(), name='discount_update'),
    path('discount/<int:pk>/delete/', views.DiscountDeleteView.as_view(), name='discount_delete'),

    # Orders
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
]
