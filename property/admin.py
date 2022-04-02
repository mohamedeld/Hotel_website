from django.contrib import admin
from .models import Property, PropertyImage, Category, PropertyReview, PropertyBook, Place
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price','avg_rating','check_avaliabilty']

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property','in_progress']
    

admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImage)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook,PropertyBookAdmin)
