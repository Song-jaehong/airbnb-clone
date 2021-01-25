from django.contrib import admin
from . import models


@admin.register(models.list)
class ListAdmin(admin.ModelAdmin):

    pass


# Register your models here.
