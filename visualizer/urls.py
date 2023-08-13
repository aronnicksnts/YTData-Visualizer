from django.urls import path
from . import views

urlpatterns = [
    path('most_viewed_creators/', views.most_viewed_creators, name='say_hello'),
]