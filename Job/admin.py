from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import Job_info


class Job_infoAdmin(admin.ModelAdmin):
    list_display = ('school_name','start_date','location', 'house','created_date')

# Now register the new UserAdmin...
admin.site.register(Job_info, Job_infoAdmin)
