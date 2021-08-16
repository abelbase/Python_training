from django.shortcuts import render
from FirstApp.models import student_info

# Create your views here.
def home_display(request):
    return render(request,'base.html')

def student_view(request):
    student_list = student_info.objects.order_by('Name')
    student_dict = {'hello':student_list}
    return render(request,'students.html',context=student_dict)
