from django.contrib import admin

# Register your models here.
from sections.models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Section, SectionAdmin)
