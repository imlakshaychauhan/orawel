from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("treatments",views.treatments,name='treatments'),
    path("login",views.login,name='login')
    # path("logout",views.logoutUser,name='logout')
]


