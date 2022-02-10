from django.urls import path 
from . import views 

urlpatterns = [ 
    path('',views.view_books),
    path('cache/',views.view_cached_books)
]