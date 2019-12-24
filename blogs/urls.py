
from . import views
from django.urls import path


urlpatterns = [
    path('write/', views.writeBlog, name='writeBlog'),
    path('display/', views.allBlogs, name='allBlog'),
]


