from django.shortcuts import render
from .models import Student, Enrollment

def index(request):
    # Query all students and their enrollments
    students = Student.objects.all()
    enrollments = Enrollment.objects.filter(student__in=students).select_related('course')

    print(students)
    return render(request, "university/index.html", {
        'students': students,
        'enrollments': enrollments
        })
