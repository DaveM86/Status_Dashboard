from django.urls import path
from diary.views import (
    DiaryListView,
    DiaryUpdateView,
    DiaryDetailView,
    AdhockTaskCreateView,
    diary_reset,
    hard_reset,
    )

urlpatterns = [
    path('', DiaryListView.as_view(), name='diary'),
    path('<int:pk>/update/', DiaryUpdateView.as_view(), name='diary-update'),
    path('adhock-create/', AdhockTaskCreateView.as_view(), name='adhock-create'),
    path('hard-reset/', hard_reset, name='hard-reset'),
    path('diary-reset/', diary_reset, name='diary-reset'),
    path('<int:pk>/', DiaryDetailView.as_view(), name='diary-detail'),
]