from django.contrib import admin

# Register your models here.
from sections.models import Section
from django import forms


class SectionModelForm(forms.ModelForm):
    content = forms.CharField(label='Vsebina', widget=forms.Textarea)

    class Meta:
        model = Section
        fields = '__all__'


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    form = SectionModelForm


admin.site.register(Section, SectionAdmin)
