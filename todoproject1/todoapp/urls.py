
from django.urls import path
from todoapp import views

urlpatterns = [

    path('',views.add,name='add'),
    # path('detail/',views.detail,name='detail')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.Todolistview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.TodoDetailview.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.TodoUpdateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.TodoDeleteview.as_view(),name='deleteview')

]
