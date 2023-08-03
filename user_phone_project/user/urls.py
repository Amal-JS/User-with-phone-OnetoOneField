from django.urls import path
from user import views

urlpatterns = [

path('',views.home,name="home"),
path("login/",views.login_user,name="login"),
path("logout/",views.logout_user,name="logout"),
path("create_account/",views.create_user,name="create_user")

]