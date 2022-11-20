from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('reservation', views.reservation, name='reservation'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('design_consultation', views.design_consultation, name='design'),

    path('post', views.PostView.as_view(), name='post'),
    path('post/<int:pk>', views.PostRetrieveView.as_view(), name='post_retrieve'),
]
