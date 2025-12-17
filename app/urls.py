from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    AboutView,
    ContactView,
    CourseList,
    CourseDetailView,
    SubjectListView,
    SubjectDetailView,
    TeacherListView,
    TeacherDetailView,
    ModuleDetailView,
    ContentDetailView,
    FeatureView,
    TeamView,
    Testimonial,
    RegisterView,
    UserLoginView,
    UserLogoutView,
    ActivateAccountView,
    ProfileView,
    EditProfileView,
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<slug:slug>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('module/<int:module_id>/', ModuleDetailView.as_view(), name='module_detail'),
    path('content/<int:content_id>/', ContentDetailView.as_view(), name='content_detail'),
    path('feature/', FeatureView.as_view(), name='feature'),
    path('team/', TeamView.as_view(), name='team'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),

]


urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
     path('profile/', ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




