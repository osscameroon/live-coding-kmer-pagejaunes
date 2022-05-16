from django.contrib import admin
from core.models import Business


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'quarter', 'sector', 'phone_number')
