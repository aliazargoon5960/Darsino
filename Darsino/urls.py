from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.url')),
    path('account/', include('account_module.url')),
    path('', include('contact_module.url')),
    path('course/', include('course_module.url')),
    path('blog/', include('blog_module.url')),
    path('cart/', include('cart_module.url')),
    path('dashboard/', include('user_panel_module.url')),
    path('tickets/', include('tickets_module.url')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
