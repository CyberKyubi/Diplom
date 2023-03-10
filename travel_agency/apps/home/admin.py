from django.contrib import admin

from . import models


admin.site.register(models.Countries)
admin.site.register(models.Replies)

