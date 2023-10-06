from django.contrib import admin
from .models import Post
# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display=('id','name','age','gender','occupation','email')
#     list_display_links=('name','email')
#     list_filter=('gender','occupation','is_married')
#     search_fields=('occupation',)
admin.site.register(Post)