from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/', views.TaskListview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:id>/', views.TaskListview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:id>/', views.TaskListview.as_view(), name='cbvupdate'),

]