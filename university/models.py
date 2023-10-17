from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gnum = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.gnum} : {self.first_name} {self.last_name}"

class Course(models.Model):
    title = models.CharField(max_length=100)
    # course registration number (ie. cs395)
    crn = models.CharField(max_length=100, primary_key=True)
    

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
    
    def isValidEnrollment(self):
        return (Enrollment.objects.filter(student=self.student, course=self.course).exists())