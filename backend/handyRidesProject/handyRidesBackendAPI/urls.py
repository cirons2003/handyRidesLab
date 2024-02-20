from django.urls import path 
from . import views


urlpatterns = [
    path('people', views.PersonCreateAPIView.as_view(), name = "people"),
    path('', views.index, name = 'index'),
    path('people/search', views.PersonSearch.as_view(), name = "city seach")
]
