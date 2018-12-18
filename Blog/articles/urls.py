from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('column/<column_slug>/',views.column_detail,name='column'),
    path('articles/<article_slug>/',views.article_detail,name='article')
]