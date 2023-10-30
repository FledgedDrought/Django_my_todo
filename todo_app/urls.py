from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('login/',views.user_login),
    path('todo/', views.todo),
    path('', views.signup),
    path('e_todo/<int:srno>',views.e_todo,name='e_todo'),
    path('del_todo/<int:srno>',views.del_todo,name='del_todo'),
    path('signout/',views.signout,name='signout'),
    
]
