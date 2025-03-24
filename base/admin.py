from django import forms
from base.models import *
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'edit_link', 'delete_link')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_per_page = 20
    
    def edit_link(self, obj):
        url = reverse("admin:base_contact_change", args=[obj.pk])
        return format_html('<a class="button" href="{}">Edit</a>', url)
    edit_link.short_description = "Edit"
    
    def delete_link(self, obj):
        url = reverse("admin:base_contact_delete", args=[obj.pk])
        return format_html('<a class="button" href="{}">Delete</a>', url)
    delete_link.short_description = "Delete"