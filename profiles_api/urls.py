from django.urls import path, include
# include list of urls in the url pattern
# arg it takes in is a list of urls

from rest_framework.routers import DefaultRouter

from profiles_api import views

# Api root: 
# includes all urls registered via the router
router = DefaultRouter()
# base_name: retrieve the url
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
