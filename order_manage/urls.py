from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login/',auth_views.login,name='login'),
    path('logout/',auth_views.logout,{'next_page': '/'},name='logout'),
    path('order/', views.order,name='order'),
    path('order/add', views.add,name='add'),
]
