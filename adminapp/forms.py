import pytz
from django import forms
from .models import Task, Feedback
from .models import StudentList

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()


class FeedbackForm:
    pass

from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'mobile_no', 'comments']


from django import forms
from .models import ContactDetail

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['name', 'email', 'mobile_no', 'address']



