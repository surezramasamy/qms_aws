
from django.urls import path
from .import views
from .views import NotificationListView,NoteCreateView,NoteUpdateView


urlpatterns = [
    path('index',views.NotificationListView.as_view(), name='index'),
    path('create',views.NoteCreateView.as_view(),name='create'),    
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='update'),

]
