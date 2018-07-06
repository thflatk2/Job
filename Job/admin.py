from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import Job_info, Job_Apply


class Job_infoAdmin(admin.ModelAdmin):
    list_display = ('school_name','start_date','location', 'house','created_date')


class Job_ApplyAdmin(admin.ModelAdmin):
    list_display = ('user','job','created_date')

# Now register the new UserAdmin...
admin.site.register(Job_info, Job_infoAdmin)
admin.site.register(Job_Apply, Job_ApplyAdmin)
