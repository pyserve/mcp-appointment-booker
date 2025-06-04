from accounts import models
from django.contrib import admin

from backend.admin import BaseModelAdmin

admin.site.register(models.UserShift, BaseModelAdmin)
