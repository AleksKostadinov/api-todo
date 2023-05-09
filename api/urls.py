from django.urls import path
from . import views


urlpatterns = [
    path('todos', views.TodoCreateList.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyList.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
]
