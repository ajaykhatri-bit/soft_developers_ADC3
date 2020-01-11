from django.urls import path
from .import views

urlpatterns = [
	path('register/', views.register, name="register"), 
	path('logout/', views.user_logout, name="logout"),
	path('login/', views.user_login, name="login"),

	#path('', views.register,name='register_insert'), # get and post req. for insert operation
    #path('<int:id>/', views.register,name='register_update'), # get and post req. for update operation
    #path('delete/<int:id>/',views.register_delete,name='register_delete'),
    #path('list/',views.registerlist,name='registerlist') # get req. to retrieve and display all records

]