# MySuperDataCompany Inc Data Upload and Query Engine

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone your-github-repo-url
   cd mysuperdatacompany
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

3. Apply database migrations:

   ```bash
   docker-compose run web python manage.py migrate
   ```

4. Access the application at `http://localhost:8000`.

## Usage

- Upload files at `http://localhost:8000/dataupload/upload/`. The form accepts CSV and JSON files.
- Query the uploaded data at `http://localhost:8000/dataupload/query/`. Optionally, filter by type using the `type` query parameter (e.g., `http://localhost:8000/dataupload/query/?type=csv`).

## Testing

- Manual testing can be performed by accessing the upload and query endpoints.

## Notes

- This proof of concept does not include authentication.
- All responses from the query view are in JSON format.
