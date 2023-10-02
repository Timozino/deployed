from django.contrib import admin

from .models import *

class What_to_learn_TabularInline(admin.TabularInline):
    model=What_to_learn
    
class Requirements_TabularInline(admin.TabularInline):
    model=Requirements
    
class Video_TabularInline(admin.TabularInline):
    model=Video

class CourseAdmin(admin.ModelAdmin):
    inlines=(What_to_learn_TabularInline, Requirements_TabularInline,Video_TabularInline)
        


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, CourseAdmin)
admin.site.register(Level)
admin.site.register(What_to_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Language)
admin.site.register(UserCourse)