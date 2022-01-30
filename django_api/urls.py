
from .  import views
from django.urls import path

urlpatterns = [
   path('first/',views.ListTodoAPIView.as_view(),name='TOdo_List'),
   path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
]