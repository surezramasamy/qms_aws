
from django.urls import path
from .import views
from .views import Instruments_Listview,Instruments_Listview2,Fixtures_Listview,Fixtures_Listview2

urlpatterns = [
    path('',views.Basic.as_view(), name='home'),    
    path('Fixtures',views.Fixtures_Listview.as_view(), name='Fixtures'),
    path('Fixtures2',views.Fixtures_Listview2.as_view(), name='Fixtures2'),
    path('Instruments',views.Instruments_Listview.as_view() , name='Instruments'),
    path('Instruments2',views.Instruments_Listview2.as_view(), name='Instruments2'),
    path('Instruments3',views.Instruments_Listview3.as_view(), name='Instruments3'),
    path('Cal',views.cal, name='Cal'),
    path('Cal2',views.cal2, name='Cal2'),

]
