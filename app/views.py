from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render
import datetime

# def footer(request):
#     current_year = datetime.now().year
#     copyright_author = "F.Timson and Technokraftz"  # Replace with your name or company name
#     return render(request, 'footer.html', {'current_year': current_year, 'copyright_author': copyright_author})


def base(request):
    # current_year = datetime.now().year
    # copyright_author = "Folorunso Timson & Technokraftz"
    return render(request, 'base.html')


def home(request):
    category=Categories.objects.all().order_by('id')[0:]
    course= Course.objects.filter(status='PUBLISH').order_by('-id')
    current_year = datetime.datetime.now().year
    copyright_author = "F.Timson and Technokraftz"
    context={}
    context['category']=category
    context['course']=course
    context['copyright_author']=copyright_author
    return render(request, 'main/home.html', context)


def single_course(request):
    category=Categories.get_all_category(Categories)
    level=Level.objects.all()
    course = Course.objects.all()
    freeCourse_count=Course.objects.filter(price=0).count()
    paidCourse_count=Course.objects.filter(price__gte=1).count()
    allCourse_count=Course.objects.all().count()
    context={}
    context['category']=category
    context['level']=level
    context['course']=course
    context['freeCourse_count']=freeCourse_count
    context['paidCourse_count']=paidCourse_count
    context['allCourse_count']=allCourse_count
    return render(request, 'main/single_course.html', context)

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    #print(price)
    
    if price == ['PriceFree']:
       course = Course.objects.filter(price=0)
       
    elif price == ['PricePaid']:
       course = Course.objects.filter(price__gte=1)
       
    elif price == ['PriceAll']:
       course = Course.objects.all()
       
    elif category:
        course = Course.objects.filter(category__id__in=category).order_by('-id')
        
    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id')
        
    else:
        course = Course.objects.all().order_by('-id')
        
    context={}
    context['course']=course
        
        
    # level = request.GET.getlist('level[]')
    # price = request.GET.getlist('price[]')
    # print(price)


    # if price == ['pricefree']:
    #    course = Course.objects.filter(price=0)
    # elif price == ['pricepaid']:
    #    course = Course.objects.filter(price__gte=1)
    # elif price == ['priceall']:
    #    course = Course.objects.all()
    # elif categories:
    #    course = Course.objects.filter(category__id__in=categories).order_by('-id')
    # elif level:
    #    course = Course.objects.filter(level__id__in = level).order_by('-id')
    # else:
    #    course = Course.objects.all().order_by('-id')


    t = render_to_string('ajax/course.html', context)

    return JsonResponse({'data': t})


def contact_us(request):
    category=Categories.get_all_category(Categories)
    context={}
    context['category']=category
    return render(request, 'main/contact_us.html', context)

def about_us(request):
    category=Categories.get_all_category(Categories)
    context={}
    context['category']=category
    return render(request, 'main/about_us.html', context)

def search_course(request):
    query=request.GET['query']
    course=Course.objects.filter(title__icontains=query)
    category=Categories.get_all_category(Categories)
    #print(course)
    context={}
    context['course']=course
    context['category']=category
    return render(request, 'search/search.html', context)
# Create your views here.

def course_details(request, slug):
    category=Categories.get_all_category(Categories)
    time_duration=Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    
    course_id = Course.objects.get(slug=slug)  
    try:
        check_enroll=UserCourse.objects.get(user=request.user, course=course_id)
        
    except UserCourse.DoesNotExist:
        check_enroll=None  
    course=Course.objects.filter(slug=slug)
    if course.exists():
        course=course.first()
    else:
        return redirect('error')
    
    # category=Categories.get_all_category(Categories)
    # time_duration=Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    context={}
    context['course']=course
    context['category']=category
    context['time_duration']=time_duration
    context['check_enroll']=check_enroll
    return render(request, 'course/course_details.html', context)

def page_not_found(request):
    category=Categories.get_all_category(Categories)
    context={}
    context['category']=category
    return render(request, 'error/404.html', context)

def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    if course.price==0:
        usercourse=UserCourse(
            user=request.user,
            course=course
        )
        usercourse.save()
        return redirect('home')
    
    course_id=Course.objects.get(slug=slug)
    try:
        enroll_status=UserCourse.objects.get(user=request.user, course=course_id)
        
    except UserCourse.DoesNotExis:
        enroll_status=None
    return render(request, 'checkout/checkout.html')

def my_course(request):
    course = UserCourse.objects.filter(user=request.user)
    context ={}
    context['course']=course
    return render(request, 'course/my-course.html', context)

def watch_course(request, slug):
    
    course=Course.objects.filter(slug=slug)
    lecture=request.GET.get('lecture')
    #course_id=Course.objects.get(id=id)
    #check_enroll=UserCourse.objects.get(user=request.user,course=course_id)
    video=Video.objects.get(id=lecture)
    # course_id=Course.objects.get(id=id)
    # course=Course.objects.filter(id=id)
    # try:
    #     check_enroll=UserCourse.objects.get(user=request.user,course=course_id)
    #     video=Video.objects.get(id=lecture)
    if course.exists():
        course=course.first()
    else:
        return redirect('404')
        
    # except UserCourse.DoesNotExist:
    #     return redirect('404')
    context={}
    context['course']=course
    context['video']=video
    context['lecture']=lecture
    return render(request, 'course/watch-course.html', context)

# @login_required
# def watch_course(request, slug):
#     # Try to get the course based on the slug, or return a 404 if it doesn't exist
#     course = get_object_or_404(Course, slug=slug)
    
#     # Get the lecture from the query parameters
#     lecture = request.GET.get('lecture')
    
#     try:
#         # Check if the user is enrolled in the course
#         check_enroll = UserCourse.objects.get(user=request.user, course=course)
        
#         # Try to get the video based on the lecture ID, or return a 404 if it doesn't exist
#         video = get_object_or_404(Video, id=lecture)
        
#     except UserCourse.DoesNotExist:
#         # Handle the case when the user is not enrolled in the course
#         return redirect('404')
    
#     context = {
#         'course': course,
#         'video': video,
#         'lecture': lecture,
#     }
    
#     return render(request, 'course/watch-course.html', context)
# def watch_course(request, id):
#     # Get the course based on the id or return a 404 response if it doesn't exist
#     course = get_object_or_404(Course, id=id)

#     # Get the lecture from the query parameters
#     lecture = request.GET.get('lecture')

#     try:
#         # Check if the user is enrolled in the course
#         check_enroll = UserCourse.objects.get(user=request.user, course=course)

#         # Try to get the video based on the lecture ID or return a 404 response if it doesn't exist
#         video = get_object_or_404(Video, id=lecture)

#     except UserCourse.DoesNotExist:
#         # Handle the case when the user is not enrolled in the course
#         return redirect('404')

#     context = {
#         'course': course,
#         'video': video,
#         'lecture': lecture,
#     }

#     return render(request, 'course/watch-course.html', context)


class AdBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.content = response.content.replace(
            b'</body>',
            b'<script src="{% static "assets/js/adblocker.js" %}"></script></body>',
        )
        return response