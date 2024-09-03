from django.urls import path
from epics import views

urlpatterns = [
    path('epics/', views.EpicList.as_view()),
    # path('epic/<int:pk>/', views.ProfileDetail.as_view())
]