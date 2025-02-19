from django.urls import path
from app import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('add/',views.add,name='add'),
    path('delete<int:id>/',views.delete,name='delete'),
    path('update<int:id>/',views.update,name='update'),
    ]
