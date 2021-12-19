from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



app_name = 'superheroes'
urlpatterns =[
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:hero_id>/edit', views.edit, name='edit'),
    path('<int:hero_id>/delete', views.delete, name='delete'),
]

# urlpatterns += staticfiles_urlpatterns()