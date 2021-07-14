from django.contrib import admin
from .models import *
# Register your models here.

# Register modeli uchun xech narsani register qilish kere emas

admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Status)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title','id']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}