from django.db import models
from datetime import datetime

from django.contrib.auth.models import User as djangouser

# Create your models here.



class Student(models.Model):
    rollNo = models.IntegerField()
    user = models.OneToOneField(djangouser,null=True,on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return self.user.username


class Assignment(models.Model):
    title=models.CharField(max_length=80,null=True)
    description=models.CharField(max_length=9999,null=True)
    start_date=models.DateField(auto_now_add=True,null=True)
    duedate = models.DateField(null=True)
    subject = models.CharField(max_length=80,null=True)

    added = models.BooleanField(default=False,)

    def add(self):
        if self.added==False:
            for student in Student.objects.all():
                ass= StudentAssignment(student=student,assignment=self)
                ass.save()
            self.added=True
            self.save()


    @property
    def get_attchments(self):
        return self.attachments.all()

    def __str__(self):
        return self.title

class StudentAssignment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,related_name="assignment")
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null= True,related_name="studentassignment")
    done=models.BooleanField(default=False)
    complete_date=models.DateField(blank=True,null=True)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.username + " : " + self.assignment.title

    @property
    def sol_title(self):
        return "Solution of " + self.assignment.title +" by " + self.student.user.username 


    

class solution(models.Model):
    
    image = models.ImageField(blank=True,null=True)
    assignment = models.ForeignKey(StudentAssignment,on_delete=models.CASCADE,null=True,related_name="solution")
    submission_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "Solution of " + self.assignment.assignment.title +" by " + self.assignment.student.user.username 
    @property
    def title(self):
        return "Solution of " + self.assignment.assignment.title +" by " + self.assignment.student.user.username 


class Attachment(models.Model):
    image = models.ImageField(blank=True,null=True)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True,related_name="attachments")

    def __str__(self):
        return "Attachment of " + self.assignment.title



