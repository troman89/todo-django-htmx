from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    ]


htmx_urlpatterns = [
    path('check_username/', views.check_username, name="check_username"),
    path('add-task/', views.add_task, name="add-task"),
    path("delete-task/<int:pk>/", views.delete_task, name="delete-task"),
    ]

urlpatterns += htmx_urlpatterns