from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("treatments",views.treatments,name='treatments'),
    path("loggedpage",views.loggedpage,name='loggedpage'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
   

]


