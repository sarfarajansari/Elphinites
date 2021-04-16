from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Attachment)
admin.site.register(StudentAssignment)
admin.site.register(solution)