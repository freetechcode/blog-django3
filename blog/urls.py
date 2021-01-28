from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:article_slug>/',
         views.article_detail,
         name='article_detail'),
    path('<int:article_id>/share/', views.article_share, name='article_share'),
]

