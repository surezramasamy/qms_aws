from django.urls import path
from .views import  HomePageView,drgupload
from . import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('drglist', DrgListView.as_view(), name='drglist'),
    path('drg', views.drg, name='drg'),
    path('drgupload/',views.drgupload, name='drgupload'),



]
