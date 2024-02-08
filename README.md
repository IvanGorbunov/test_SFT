# Test task from SFT

--- 
### Features:

List of endpoints:

   ```angular2html
   http://127.0.0.1:8031/admin/ - admin panel
   http://127.0.0.1:8031/swagger/ - documents for API
   http://127.0.0.1:8031/api/unique-producers-of-loan-applications-products/{pk}}/ - unique pk`s of producers by pk of loan application  
   ```


---
## Installation:

1. Clone the repository:
   
    ```bash
   git clone https://github.com/IvanGorbunov/test_SFT.git
   ```
   
2. Create and fill up a `.env` file according to the template `/src/settings/.env.template`. The `.env` file must be in the directory: `src/config/settings/`.
   
    ```
    DEBUG=True
    SQL_DEBUG=True
    DJANGO_LOG_LEVEL=INFO
    SECRET_KEY=
    DJANGO_ALLOWED_HOSTS=*
    STATIC_ROOT=var/www/staticfiles
    DATABASE_URL=psql://postgres:postgres@127.0.0.1:5437/test_sft
    DATABASE_URL_IN_DOCKER=psql://postgres:postgres@db:5432/test_sft
    RUN_IN_DOCKER=True
    ```

### Run in docker

```bash
docker-compose up -d --build
```

### Run locally

1. Install all necessary package from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
   
2. Run a migration:

    ```bash
    python3 ./src/manage.py migrate
    ```
   
3. Create a superuser:

    ```bash
    python3 ./src/manage.py add_superuser
    ```

4. Collect static files:

    ```bash
    python3 ./src/manage.py collectstatic
    ```
   
5. Run server:

    ```bash
    python3 ./src/manage.py runserver
    ```
