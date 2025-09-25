from django.contrib import admin
from .models import Ticket, TicketReply, TicketAttachment
from django.utils.html import format_html


class TicketReplyInline(admin.TabularInline):
    model = TicketReply
    extra = 0
    readonly_fields = ('created_at',)

class TicketAttachmentInline(admin.TabularInline):
    model = TicketAttachment
    extra = 0
    readonly_fields = ('file_link',)

    def file_link(self, obj):
        if obj.file:
            return format_html(f"<a href='{obj.file.url}' target='_blank'>{obj.file.name}</a>")
        return "-"
    file_link.short_description = "فایل"


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id','subject','user','status','priority','created_at','updated_at')
    list_filter = ('status','priority','created_at')
    search_fields = ('subject','message','user__username','user__email')
    inlines = (TicketReplyInline, TicketAttachmentInline)

@admin.register(TicketReply)
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ('ticket','user','created_at')
