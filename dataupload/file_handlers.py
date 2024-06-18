import csv
import json
from abc import ABC, abstractmethod
from .models import FileUpload, DataRecord

class FileHandlerStrategy(ABC):
    @abstractmethod
    def handle(self, file, upload):
        pass

class CSVFileHandler(FileHandlerStrategy):
    def handle(self, file, upload):
        print("Handling CSV file")
        file.seek(0)  # Ensure we are at the start of the file
        file_content = file.read().decode('utf-8')
        print(f"File content: {file_content}")
        if not file_content:
            print("Error: File content is empty")
            return
        reader = csv.DictReader(file_content.splitlines())
        for row in reader:
            print(f"CSV Row: {row}")
            for key, value in row.items():
                print(f"Inserting CSV Record: {key}={value}")
                try:
                    DataRecord.objects.create(upload=upload, key=key, value=value, type='csv')
                    print(f"Record inserted: {key}={value}")
                except Exception as e:
                    print(f"Error inserting record: {e}")

class JSONFileHandler(FileHandlerStrategy):
    def handle(self, file, upload):
        print("Handling JSON file")
        file.seek(0)  # Ensure we are at the start of the file
        try:
            data = json.load(file)
            print(f"JSON Data: {data}")
            for key, value in data.items():
                print(f"Inserting JSON Record: {key}={value}")
                try:
                    DataRecord.objects.create(upload=upload, key=key, value=value, type='json')
                    print(f"Record inserted: {key}={value}")
                except Exception as e:
                    print(f"Error inserting record: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

def get_file_handler(file_type):
    if file_type == 'csv':
        return CSVFileHandler()
    elif file_type == 'json':
        return JSONFileHandler()
    else:
        raise ValueError('Unsupported file type')
