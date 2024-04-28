from django.urls import path
from acesecurity import views

urlpatterns = [
    path("select/", views.selectView, name="select_data"),
    path("insert/", views.insertView, name="insert_data"), 
    path("update/", views.updateView, name="update_data"),
    path("delete/", views.deleteView, name="delete_data"),
    path("reports/", views.reportView, name="reports"),
    path("", views.home, name="home"),
]