from django.apps import apps
from django.contrib import admin

for i in apps.get_app_config('my_app').models.values():
    admin.site.register(i)
