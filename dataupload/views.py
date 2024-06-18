from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UploadFileForm
from .models import FileUpload, DataRecord  
from .file_handlers import get_file_handler

class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to MySuperDataCompany Inc!")

class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'upload.html'
    success_url = reverse_lazy('upload_success')

    def form_valid(self, form):
        file = self.request.FILES['file']
        print(f"Received file: {file.name}")
        if file.name.endswith('.csv'):
            file_type = 'csv'
        elif file.name.endswith('.json'):
            file_type = 'json'
        else:
            return JsonResponse({'error': 'Invalid file type'}, status=400)

        upload = FileUpload.objects.create(file=file, file_type=file_type)
        print(f"Created FileUpload: {upload}")
        handler = get_file_handler(file_type)
        handler.handle(file, upload)
        print("File handled successfully")

        return super().form_valid(form)

class UploadSuccessView(View):
    def get(self, request):
        return JsonResponse({'message': 'File uploaded successfully'})

class QueryDataView(View):
    def get(self, request):
        data_type = request.GET.get('type', None)
        if data_type:
            records = DataRecord.objects.filter(type=data_type)
        else:
            records = DataRecord.objects.all()

        data = [{'key': record.key, 'value': record.value} for record in records]
        print(f"Queried Data: {data}")
        return JsonResponse(data, safe=False)
