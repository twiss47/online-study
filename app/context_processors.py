from .models import Subject, Course

def subjects_processor(request):
    subjects = Subject.objects.all()
    return {'subjects': subjects}





def header_courses(request):
    return {"courses": Course.objects.all()}




def subjects_processor(request):
    return {'subjects': Subject.objects.all()}

def header_courses(request):
    return {'courses': Course.objects.all()}