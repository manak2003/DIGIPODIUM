from atexit import register
from django.contrib import admin
from .models import Movies , Show, Student, Report, Weather, Singer

admin.site.register(Movies) #this line add your table to admin dashboard
admin.site.register(Show)


@admin.register(Student)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('rollno','klass','name')
    search_fields = ('name','klass')
    ordering = ('name',)
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
        '''Admin View for '''
    
        list_display = ('student','english','hindi','maths','science','socialscience','computer')

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    '''Admin View for Weather'''

    list_display = ('date','temp','humidity','wind_speed')
    list_filter = ('date',)
    ordering = ('date',)
    
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title','artist','audio_file')
    list_filter = ('title',)
    ordering = ('title',)