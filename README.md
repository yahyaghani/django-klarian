# MySuperDataCompany

## Description
This is a Django application for uploading and querying JSON and CSV files.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yahyaghani/django-klarian
    cd mysuperdatacompany
    ```

2. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Apply migrations:
    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. Create a superuser (optional):
    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

5. Access the application at [http://localhost:8000](http://localhost:8000).

## Usage

- Upload files at [http://localhost:8000/upload/](http://localhost:8000/upload/).
- Query data at [http://localhost:8000/query/](http://localhost:8000/query/).

## Authors
- Yahya Ghani

