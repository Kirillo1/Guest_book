from django.contrib import admin

from book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'post_text']
    list_filter = ['time_of_creation']
    search_fields = ['name', 'status']
    fields = ['name', 'status', 'post_text', 'mail', 'time_of_creation', 'update_time']
    readonly_fields = ['time_of_creation', 'update_time']


admin.site.register(GuestBook, GuestBookAdmin)
