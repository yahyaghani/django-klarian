# Dockerfile

# Pull official base image
FROM python:3.10

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Add entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh

# Make entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Command to run the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysuperdatacompany.wsgi:application"]
