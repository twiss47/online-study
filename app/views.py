from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views import View
from django.views.generic import TemplateView
from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from .models import (
    Course,
    Teacher,
    Subject,
    Module,
    Content,
    Profile

)


#FOR EMAIL CONFIRM
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site




#============= Home =============

class HomeView(TemplateView):
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['teachers'] = Teacher.objects.filter(is_active=True)
        return context
    


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'


class FeatureView(TemplateView):
    template_name = 'home/feature.html'


class Testimonial(TemplateView):
    template_name = 'home/testimonial.html'




#============= Course =============

class CourseList(ListView):
    model = Course
    template_name = 'home/courses.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = "home/detail.html"
    context_object_name = "course"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.modules.all()
        context['courses'] = Course.objects.all()  
        return context





#============= Subject =============

class SubjectListView(ListView):
    model = Subject
    template_name = "home/subject_list.html"
    context_object_name = "subjects"

class SubjectDetailView(DetailView):
    model = Subject
    template_name = "home/subject_detail.html"
    context_object_name = "subject"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.courses.all()
        return context




#============= Teachers =============

class TeacherListView(ListView):
    model = Teacher
    template_name = "home/teacher_list.html"
    context_object_name = "teachers"

    def get_queryset(self):
        return Teacher.objects.filter(is_active=True)

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "home/teacher_detail.html"
    context_object_name = "teacher"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.courses.all()
        return context



#============= Module =============

class ModuleDetailView(DetailView):
    model = Module
    template_name = "home/module_detail.html"
    pk_url_kwarg = 'module_id'
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contents'] = self.object.contents.all()
        return context


#============= Content =============

class ContentDetailView(View):
    def get(self, request, content_id):
        content = get_object_or_404(Content, id=content_id)
        item = content.item
        template_map = {
            'text': 'home/text.html',
            'image': 'home/image.html',
            'video': 'home/video.html',
            'file': 'home/file.html',
        }
        model_name = content.content_type.model
        return render(request, template_map[model_name], {'item': item})
    




#============= Some View =============

class SomeView(ListView):
    model = Subject
    template_name = "home/template.html"
    context_object_name = "subjects"




#============= Team View =============

class TeamView(ListView):
    model = Teacher
    template_name = "home/team.html"
    context_object_name = "teachers"

    def get_queryset(self):
        return Teacher.objects.filter(is_active=True)
    




# Login
class UserLoginView(LoginView):
    template_name = "home/login.html"
    redirect_authenticated_user = True

# Logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('app:home')
    require_POST = False

# Register
class RegisterView(View):
    def get(self, request):
        return render(request, 'home/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'home/register.html', {'error': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'home/register.html', {'error': 'Email already exists.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = request.build_absolute_uri(
            reverse_lazy('app:activate', kwargs={'uidb64': uid, 'token': token})
        )

        message = f"Hi {user.username}, please click the link to activate your account: {activation_link}"
        send_mail(
            'Activate your account',
            message,
            'REMOVED',  
            [user.email],
            fail_silently=False,
        )

        return render(request, 'home/registration_pending.html')

# Activate
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'home/activation_success.html', {'message': "Your account is now active! You can login."})
        else:
            return render(request, 'home/activation_invalid.html', {'message': "Activation link is invalid or expired."})

# Profile View
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('app:login')

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'home/profile.html', {'profile': profile})







class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['avatar', 'bio', ] 
    success_url = reverse_lazy('app:profile')  

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    



class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'home/profile_form.html'
    success_url = reverse_lazy('app:profile') 

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile