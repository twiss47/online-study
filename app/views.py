from django.shortcuts import render, get_object_or_404
from .models import Subject, Course, Teacher, Module, Content
from django.contrib.contenttypes.models import ContentType

# Home & About
def home(request):
    courses = Course.objects.all()
    return render(request, 'home/index.html', {'courses': courses})


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

# Courses
def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'home/courses.html', {'courses': all_courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.all()
    return render(request, 'home/detail.html', {
        'course': course,
        'modules': modules,
    })

# Additional Pages
def feature(request):
    return render(request, 'home/feature.html')

def team(request):
    return render(request, 'home/team.html')

def testimonial(request):
    return render(request, 'home/testimonial.html')

# Subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'home/subject_list.html', {'subjects': subjects})


def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    courses = subject.courses.all()
    return render(request, 'home/subject_detail.html', {
        'subject': subject,
        'courses': courses
    })

# Teachers
def teacher_list(request):
    teachers = Teacher.objects.filter(is_active=True)
    return render(request, 'home/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    courses = teacher.courses.all()
    return render(request, 'home/teacher_detail.html', {
        'teacher': teacher,
        'courses': courses,
    })

# Modules
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    contents = module.contents.all()
    return render(request, 'home/module_detail.html', {
        'module': module,
        'contents': contents
    })

# Content
def content_detail(request, content_id):
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



def some_view(request):
    subjects = Subject.objects.all()
    return render(request, 'home/template.html', {'subjects': subjects})