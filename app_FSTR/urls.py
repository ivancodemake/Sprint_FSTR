from django.urls import path
from .views import get_data, update_data, MountainList, reverse_to_submit, MountainCreate, ImageViewSet


urlpatterns = [
    path('submitData/', MountainList.as_view({'get': 'list'}), name='submitData'),
    path('submitData/create/', MountainCreate.as_view(), name='create'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
    path('submitData/<int:pk>/update/', update_data, name='update_data'),
    path('submitData/upload/', ImageViewSet.as_view(), name='upload'),
    path('', reverse_to_submit),
]


