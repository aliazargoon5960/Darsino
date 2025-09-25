from django.urls import path
from . import views

app_name = 'tickets_module'

urlpatterns = [
    path('', views.TicketListView.as_view(), name='ticket_list'),
    path('new/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/reply/', views.TicketReplyView.as_view(), name='ticket_reply'),
]
