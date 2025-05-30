from django.contrib import admin

# admin.py
from django.contrib import admin
from .models import jhexam
from django.contrib.auth.models import User
from django import forms
from django.utils.html import format_html

class jhexamAdminForm(forms.ModelForm):
    class Meta:
        model = jhexam
        fields = '__all__'

class jhexamAdmin(admin.ModelAdmin):
    form = jhexamAdminForm
    list_display = ('exam_name', 'created_at', 'exam_date', 'is_public', 'display_users')
    list_filter = ('is_public', 'created_at')
    search_fields = ('exam_name', 'users__email')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'
    
    def display_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])
    display_users.short_description = "Пользователи"

admin.site.register(jhexam, jhexamAdmin)
