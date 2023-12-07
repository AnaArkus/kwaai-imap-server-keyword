# Kwaai AI Lab - IMAP server

## Docker Compose Setup for Django App and PostgreSQL

This Docker Compose configuration is designed for a Django app and PostgreSQL database.

## Services

### 1. app

- **Build**: The Django app is built from the current context (`.`) with the DEV flag set to true.
- **Ports**: The app is exposed on port 8000.
- **Volumes**:
  - `./app` is mounted to `/app` in the container.
  - `dev-static-data` is mounted to `/vol/web` for static data.
- **Command**: Runs Django management commands (`wait_for_db`, `migrate`, and `runserver`) on startup.
- **Environment**:
  - `DB_HOST`: Database host name (`db`).
  - `DB_NAME`: Database name (`devdb`).
  - `DB_USER`: Database user (`devuser`).
  - `DB_PASS`: Database password (`changeme`).
  - `DEBUG`: Enables Django debug mode (`1`).

### 2. db

- **Image**: PostgreSQL 13 Alpine.
- **Volumes**: `dev-db-data` is mounted to `/var/lib/postgresql/data` for persistent data.
- **Environment**:
  - `POSTGRES_DB`: PostgreSQL database name (`devdb`).
  - `POSTGRES_USER`: PostgreSQL database user (`devuser`).
  - `POSTGRES_PASSWORD`: PostgreSQL database password (`changeme`).

## Dependencies

- The `app` service depends on the `db` service.

## How to Use

1. Ensure Docker and Docker Compose are installed.
2. Run the following command in the project root directory to build and start the services:

   ```bash
   docker-compose up --build
   ```

3. The Django app will be accessible at `http://localhost:8000`.

4. Swagger API Documentation:
   - Visit `http://localhost:8000/api/docs/` to access Swagger documentation for the API services.

## Notes

- Ensure proper adjustments to environment variables (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASS`) for production use.
- Debug mode is enabled in this setup; it's recommended to disable it in a production environment.
- The `depends_on` section ensures that the `app` service starts after the `db` service.

For additional configurations and deployment considerations, refer to the documentation of Django and PostgreSQL.
```

Feel free to let me know if you have any other requests or if you'd like further adjustments!