from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius: 50px" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designatiom', 'created_date')
    list_display_links = ('first_name', 'thumbnail', 'id')
    search_fields = ('first_name', 'last_name', 'designatiom',)
    list_filter = ('designatiom',)


admin.site.register(Team, TeamAdmin)