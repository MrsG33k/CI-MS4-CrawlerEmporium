from django.contrib import admin
from .models import SupportTicket

# Register your models here.

@admin.register(SupportTicket)
class SupportTicktAdmin(admin.ModelAdmin):
    list_display = (
        'ticket_id_string',
        'user',
        'full_name',
        'email',
        'severity',
        'is_resolved',
        'created_at'
    )

    list_filter = ('is_resolved', 'severity', 'created_at')

    search_fields = ('full_name', 'email', 'subject', 'message')

    ordering = ['-id']

    readonly_fields = ['created_at']

    #Appends Tick# onto the front of the Ticket ID admin panel
    @admin.display(description="TICK#", ordering="ticket_id_string")
    def ticket_id_string(self, obj):
        return obj.id
