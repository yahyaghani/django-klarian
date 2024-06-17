from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=10)  # json or csv

class DataRecord(models.Model):
    upload = models.ForeignKey(FileUpload, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=50)  # Optional query parameter
