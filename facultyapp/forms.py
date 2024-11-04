from django import forms
from .models import FacultyPost

class FacultyPostForm(forms.ModelForm):
    class Meta:
        model = FacultyPost
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }
        labels = {
            'title': 'Blog Title',
            'content': 'Write Your Blog',
        }
from django import forms
from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model=AddCourse
        fields=['student','course','section']

from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields=['student','course','marks']