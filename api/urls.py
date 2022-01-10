from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverView, name='api-overview'),
	path('task-list/', views.taskList, name='task-list'),
	path('task-list/<str:pk>/', views.taskDetail, name='task-detail'),
	path('task-create/', views.taskCreate, name='task-create'),
	path('task-update/<str:pk>', views.taskUpdate, name='task-update'),
]


