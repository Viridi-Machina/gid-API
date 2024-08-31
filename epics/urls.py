from django.urls import path
from profiles import views

urlpatterns = [
    path('epics/', views.ProfileList.as_view()),
    # path('epic/<int:pk>/', views.ProfileDetail.as_view())
]