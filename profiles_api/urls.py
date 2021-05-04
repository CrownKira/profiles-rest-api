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
# if provide the queryset, base name is not needed
# cos DRF can figure out the name from the model that is assigned to it 
# base_name: only needed when there is no queryset assigned to it
# / when you want to override the name
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
