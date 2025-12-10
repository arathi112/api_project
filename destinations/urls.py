from django.urls import path
from . import views

urlpatterns = [
    # API URLs
    path('api/destinations/', views.DestinationListCreateAPIView.as_view(), name='destination-list-create'),
    path('api/destinations/<int:pk>/', views.DestinationRetrieveUpdateDestroyAPIView.as_view(),
         name='destination-retrieve-update-destroy'),
    path('api/images/<int:image_id>/', views.DeleteDestinationImageAPIView.as_view(), name='delete-image'),

    # Template URLs
    path('', views.destination_list, name='destination-list-page'),
    path('create/', views.destination_create, name='destination-create-page'),
    path('<int:pk>/', views.destination_detail, name='destination-detail-page'),
    path('<int:pk>/update/', views.destination_update, name='destination-update-page'),
]