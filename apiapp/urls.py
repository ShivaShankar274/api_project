from django.urls import path
from apiapp import views

urlpatterns=[
    path('read/',views.read_api),
    path('create/',views.create_api),
    path('update/<int:id>/',views.update_api),
    path('delete/<int:id>/',views.delete_api),
    path('view/<str:uname>/',views.view_api),
]