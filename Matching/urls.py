from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('questions/', views.questions, name='questions'),
    path('show_matches/', views.show_matches, name='show_matches'),
    path('swipeCard/<int:pk>',views.swipeCard,name='swipeCard')

]