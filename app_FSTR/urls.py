from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('submitData/', MountainList.as_view({'get': 'list'}), name='submitData'),   # Получить список всех созданных объявлений
    path('api/submitData/create/', MountainCreate.as_view(), name='create'),         # Создание объявлений с помощью браузерной формы
    path('submitData/submit/', submit_data, name='submit_data'),                     # Создание объявлений в json формате
    path('submitData/<int:pk>/', get_data, name='get_data'),                         # Получить объявление по id
    path('submitData/<int:pk>/update/', update, name='update'),                      # Обновить/редактировать объявление в json формате
    path('api/submitData/<int:pk>/update/', Update.as_view(), name='patch'),         # Обновить/редактировать объявление с помощью браузерной формы
    path('submitData/upload/', ImageViewSet.as_view(), name='upload'),               # Загрузить фото через браузерную форму
    re_path(r'^swagger(\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    # Получить документацию через оболочку SWAGGER
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', reverse_to_submit)
]


