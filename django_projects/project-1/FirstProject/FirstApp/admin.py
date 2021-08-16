from django.contrib import admin
from FirstApp.models import student_info
# Register your models here.
# class StudentAdmin(admin.ModelAdmin):
#     list_display =['Name',"IDs","Contact"]

admin.site.register(student_info)
