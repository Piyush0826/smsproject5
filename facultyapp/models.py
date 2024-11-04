from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from adminapp.models import StudentList



class FacultyPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class AddCourse(models.Model):
    COURSE_CHOICES=[
        ('AOOP','Advanced Object-Oreinted Programming'),
        ('PFSD','Python Full Stack Development'),
        ('DBMS','Database Management System'),
        ('NPS','Network Protocol and Security'),
    ]
    SECTION_CHOICES=[
        ('S11','Section 11'),
        ('S12', 'Section 12'),
        ('S13', 'Section 13'),
        ('S14', 'Section 14'),
        ('S15', 'Section 15'),
    ]
    student=models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    section=models.CharField(max_length=50,choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES=[
        ('AOOP', 'Advanced Object-Oreinted Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('DBMS', 'Database Management System'),
        ('NPS', 'Network Protocol and Security'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    marks=models.IntegerField()
    def __str__(self):
        return f"{self.student.name}-{self.course}"