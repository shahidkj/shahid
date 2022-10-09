
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvlistview/',views.tasklistview.as_view(),name='tasklistview'),
    path('cbvdetailview/<int:pk>/',views.taskdetailview.as_view(),name='taskdetailview'),
    path('cbvupdateview/<int:pk>/', views.taskupdateview.as_view(), name='taskupdateview'),
    path('cbvdeleteview/<int:pk>/', views.taskdeleteview.as_view(), name='taskdeleteview'),
]
