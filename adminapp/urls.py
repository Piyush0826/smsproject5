from django.urls import path

from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionalpagelogic/', views.exceptionalpagelogic, name='exceptionalpagelogic'),
    path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('randompagecall/',views.randompagecall, name='randompagecall'),
    path('calculatorpagelogic/',views.calculatorpagelogic,name='calculatorpagelogic'),
    path('calculatorpagecall/',views.calculatorpagecall, name='calculatorpagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('datetimepagecall/',views.datetimepagecall, name='datetimepagecall'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task, name='delete_task'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('upload_files/',views.upload_files,name='upload_files'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('contact_list/', views.contact_list, name='contact_list'),

]
