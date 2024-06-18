from django.urls import path
from .views import UploadFileView, UploadSuccessView, QueryDataView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('upload/success/', UploadSuccessView.as_view(), name='upload_success'),
    path('query/', QueryDataView.as_view(), name='query_data'),
]
