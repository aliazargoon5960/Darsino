from django import forms
from .models import Ticket, TicketReply, TicketAttachment


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message', 'priority']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع تیکت'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن تیکت'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }



class TicketReplyForm(forms.ModelForm):
    files = forms.FileField(widget=MultiFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = TicketReply
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پاسخ خود را وارد کنید'}),
        }

    def save(self, commit=True, reply_user=None, ticket=None, files=None):
        reply = super().save(commit=False)
        if reply_user:
            reply.user = reply_user
        if ticket:
            reply.ticket = ticket
        if commit:
            reply.save()
            # ذخیره فایل‌ها
            if files:
                for f in files:
                    TicketAttachment.objects.create(reply=reply, file=f)
        return reply




class TicketAttachmentForm(forms.ModelForm):
    class Meta:
        model = TicketAttachment
        fields = ['file']
        widgets = {
            'file': MultiFileInput(attrs={'class': 'form-control', 'multiple': True}),
        }

