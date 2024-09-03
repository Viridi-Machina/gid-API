from django.urls import path
from epics import views

urlpatterns = [
    path('epics/', views.EpicList.as_view()),
    path('epics/<int:pk>/', views.EpicDetail.as_view())
]