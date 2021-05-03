from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Content, Comment

admin.site.register(Content)
admin.site.register(Comment)
