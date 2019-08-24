from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('todo/<int:pk>/', DetailTodo.as_view()),
    path('todos/', ListTodo.as_view()),
]
