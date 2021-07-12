from . import views

from django.urls import path, include

urlpatterns = [

    path('tasks/', views.TaskListCreate.as_view()),
    path('tasks/completed/', views.TaskListCompleted.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view()),
    path('tasks/<int:pk>/complete/', views.TaskComplete.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
