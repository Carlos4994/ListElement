from django.contrib import admin

# Register your models here.
from .models import Element,Category,Type


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Type,TypeAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Element,ElementAdmin)
