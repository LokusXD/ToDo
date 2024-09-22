from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/nearest/', views.NearestTask.as_view()),
    path('tasks/creation/', views.TaskListCreate.as_view()),
    path('tasks/<pk>/', views.TaskDetail.as_view()),
    path('tasks/<pk>/update/', views.TaskUpdate.as_view()),
    path('tasks/<pk>/delete/', views.TaskDelete.as_view()),  
    path('leetcode/array/', views.RotateArray.as_view()),
    path('leetcode/kth_longest/', views.KthLargestElement.as_view()),
    path('leetcode/longest_path/', views.LongestIncreasingPath.as_view()),
]