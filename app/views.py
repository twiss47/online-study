from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import (
    Course,
    Teacher,
    Subject,
    Module,
    Content

)

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