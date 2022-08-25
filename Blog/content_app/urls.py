from django.urls import path
from content_app import views

urlpatterns = [
    path('home/',views.home, name ='home'),
    path('',views.home),
    path('add-blog/',views.add_blog,name='add-blog'),
    path('delete-blog/<int:id>',views.delete_blog,name='delete-blog'),
    path('edit-blog/<int:id>',views.edit_blog,name='edit-blog'),
    path('404/',views.not_found,name='404')
]