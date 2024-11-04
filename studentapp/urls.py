from django.urls import path

from . import views
app_name = 'studentapp'
urlpatterns = [
 path('student/',views.studentconsole,name='student'),
 path('StudentHomePage/',views.StudentHomePage,name='StudentHomePage'),
 path('view_marks/',views.view_marks,name='view_marks')
]
