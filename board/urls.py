"""dashboard_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import DSSListView, DSSUpdateView, CommentCreateView, SoftwareUpdateView, DeploymentListView, BuildUpdateView

urlpatterns = [
    path('', DSSListView.as_view(), name='board-home'),
    path('<int:pk>/update/', DSSUpdateView.as_view(), name='DSS-update'),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/software/update/', DSSUpdateView.as_view(), name='software-update'),
    path('deployment/', DeploymentListView.as_view(), name='deployment'),
    path('<int:pk>/build/update/', BuildUpdateView.as_view(), name='build-update'),
]