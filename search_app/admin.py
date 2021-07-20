from django.contrib import admin
from .models import Index

# Register your models here.

class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

    class Meta:
        verbose_name_plural = 'Index'

admin.site.register(Index, IndexAdmin)