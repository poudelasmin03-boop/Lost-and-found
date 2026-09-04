from django.contrib import admin
from .models import Itemdetails


@admin.register(Itemdetails)
class ItemdetailsAdmin(admin.ModelAdmin):
    list_display = ('itemName', 'user', 'location', 'foundDate', 'itemTag', 'phoneNo', 'created_at')
    list_filter = ('itemTag', 'foundDate', 'location')
    search_fields = ('itemName', 'itemDescription', 'location', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
