from django.contrib import admin
from home.models import School
# Register your models here.
# admin.site.register(School)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display =['id','name','school_unique_code','address','is_active','created_at','updated_at']
    list_filter = ['is_active']
    search_fields = ['name']
    list_display_links = ['address']
    list_editable = ['school_unique_code','name']