from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'created_at')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author')
        }),
        ('Publication Details', {
            'fields': ('publication_year',),
            'classes': ('collapse',)
        }),
    )

