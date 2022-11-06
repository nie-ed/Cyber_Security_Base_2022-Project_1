from django.urls import path


from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('newuser/', views.createnew, name='new'),
    path('add/', views.add, name='add'),


]