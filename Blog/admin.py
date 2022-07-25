from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


# Kabbo Liate
# Stela Anderson
# Aveta Deb
# Sona Terner

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_as = True
    list_display = ['id', 'title', 'slug', 'created_at', 'get_photo', 'views']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tage']
    search_fields = ['title']
    readonly_fields = [ 'created_at', 'views', 'get_photo']
    fields = ['title', 'slug', 'category', 'tage', 'content', 'get_photo', 'photo', 'views', 'created_at', ]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'photo'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tage, TageAdmin)
