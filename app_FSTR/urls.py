from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('submitData/', MountainList.as_view({'get': 'list'}), name='submitData'),   # Получить список всех созданных объявлений
    path('submitData/create/', MountainCreate.as_view(), name='create'),             # Создание объявлений через форму REST Framework
    path('submitData/submit/', submit_data, name='submit_data'),                     # Создание объявлений в json формате
    path('submitData/<int:pk>/', get_data, name='get_data'),                         # Получить объявление по pk ключу
    path('submitData/<int:pk>/update/', update_data, name='update_data'),            # Обновить/редактировать объявление
    path('submitData/upload/', ImageViewSet.as_view(), name='upload'),               # Загрузить фото через форму REST Framework
    re_path(r'^swagger(\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    # Получить документацию через оболочку SWAGGER
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', reverse_to_submit)
]


