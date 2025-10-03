from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.urls import reverse_lazy
from .models import Ticket, TicketReply, TicketAttachment
from .forms import TicketCreateForm, TicketReplyForm


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets_module/ticket_list.html'
    context_object_name = 'tickets'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketCreateForm
    template_name = 'tickets_module/ticket_create.html'
    success_url = reverse_lazy('tickets_module:ticket_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        files = self.request.FILES.getlist('files')
        for f in files:
            TicketAttachment.objects.create(ticket=self.object, file=f)

        return response


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'tickets_module/ticket_detail.html'
    context_object_name = 'ticket'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_form'] = TicketReplyForm()
       
        context['ticket_attachments'] = self.object.attachments.filter(reply__isnull=True)
        return context


class TicketReplyView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        form = TicketReplyForm(request.POST) 
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.user = request.user
            reply.save()

            files = request.FILES.getlist('files')
            for f in files:
                TicketAttachment.objects.create(reply=reply, file=f)

            ticket.status = Ticket.STATUS_PENDING
            ticket.save()

        return redirect('tickets_module:ticket_detail', pk=pk)
        
