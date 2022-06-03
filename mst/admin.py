from django.contrib import admin
from .models import Member
from .models import Group

# Register your models here.
admin.site.register(Member)
admin.site.register(Group)