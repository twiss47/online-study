from django.urls import path
from .views import (
    home,
    about,
    courses,
    subject_list,
    subject_detail,
    course_detail,
    teacher_list,
    teacher_detail,
    module_detail,
    content_detail,
    feature,
    team,
    testimonial,
    contact
)

app_name = 'app'  

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
    path('courses/<slug:slug>/', course_detail, name='course_detail'),
    path('subjects/', subject_list, name='subject_list'),
    path('subjects/<slug:slug>/', subject_detail, name='subject_detail'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
    path('module/<int:module_id>/', module_detail, name='module_detail'),
    path('content/<int:content_id>/', content_detail, name='content_detail'),
    path('feature/', feature, name='feature'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]
