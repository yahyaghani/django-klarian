import csv
import json
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import FileUpload, DataRecord
from django.http import JsonResponse

def handle_uploaded_file(file, file_type):
    upload = FileUpload.objects.create(file=file, file_type=file_type)
    if file_type == 'csv':
        reader = csv.DictReader(file.read().decode('utf-8').splitlines())
        for row in reader:
            for key, value in row.items():
                DataRecord.objects.create(upload=upload, key=key, value=value, type='csv')
    elif file_type == 'json':
        data = json.load(file)
        for key, value in data.items():
            DataRecord.objects.create(upload=upload, key=key, value=value, type='json')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                handle_uploaded_file(file, 'csv')
            elif file.name.endswith('.json'):
                handle_uploaded_file(file, 'json')
            else:
                return JsonResponse({'error': 'Invalid file type'}, status=400)
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return JsonResponse({'message': 'File uploaded successfully'})

def query_data(request):
    data_type = request.GET.get('type', None)
    if data_type:
        records = DataRecord.objects.filter(type=data_type)
    else:
        records = DataRecord.objects.all()

    data = [{'key': record.key, 'value': record.value} for record in records]
    return JsonResponse(data, safe=False)
