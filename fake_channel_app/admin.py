from django.contrib import admin
from .models import OrgConfig, Contact, ResponseSet


@admin.register(OrgConfig)
class OrgConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ResponseSet)
class ResposeSetAdmin(admin.ModelAdmin):
    list_display = ["number_of_response", "text_of_response"]
    ordering = ['number_of_response']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["number", "requests_count"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return True
