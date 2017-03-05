from django.contrib import admin
from apps.catalogue.models import Store


admin.site.register(Store)

from oscar.apps.catalogue.admin import *  # noqa


