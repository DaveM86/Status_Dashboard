from django.contrib import admin
from .models import DSS, Comment, SoftwareUpdate, Deployment

admin.site.register(DSS)

admin.site.register(Comment)

admin.site.register(SoftwareUpdate)

admin.site.register(Deployment)
