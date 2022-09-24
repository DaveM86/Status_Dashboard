from django.contrib import admin
from .models import DSS, Comment, SoftwareUpdate, Deployment, InBuild, BuildStages, DatesOfBuildStages

admin.site.register(DSS)

admin.site.register(Comment)

admin.site.register(SoftwareUpdate)

admin.site.register(Deployment)

admin.site.register(InBuild)

admin.site.register(BuildStages)

admin.site.register(DatesOfBuildStages)