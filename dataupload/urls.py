from django.urls import path
from .views import upload_file, upload_success, query_data

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    path('query/', query_data, name='query_data'),
]
