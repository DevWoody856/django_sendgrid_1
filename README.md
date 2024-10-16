
This is the repository for <a href="https://rx-36.life/create-a-contact-form-using-sendgrid-with-django/" target="_blank"><span class="link">this blog post</span></a>.


It demonstrates a simple application: "Creating a contact form using SendGrid with Django".

## How to download and run this application locally

This guide assumes you're using Docker on Windows 11. I'm using PyCharm as my IDE.


1. Clone the repository:
```
git clone https://github.com/DevWoody856/django_sendgrid_1.git
```

2. Create an `.env` file in the project's root directory.

3. Populate the `.env` file with the following values:

```
DEBUG_VALUE=TRUE
SECRET_KEY=******************************************

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db_send_grid_241015
DB_PORT=5432

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

SENDGRID_API_KEY=******************************************

TO_EMAIL=********@*********.***
```

Remember to replace the placeholder values for `SECRET_KEY`, `SENDGRID_API_KEY`, and `TO_EMAIL` with your own credentials. DB_HOST should match the database service name defined in docker-compose.yaml (in this case, `db_send_grid_241015`).


4. Start the Docker containers:

```bash
docker-compose up --build
```

5. Once you see the message "Starting development server at http://0.0.0.0:8002/", open another terminal and enter the following command to access the backend container's command line:

```bash
docker-compose exec backend bash
```

6. With the database setup complete, start the Django development server:

```bash
python manage.py runserver
```

7. The application is running successfully if you see:

```bash
Starting development server at http://127.0.0.1:8002/.
```

### The actual application is accessed at `http://127.0.0.1:8002/`. Please note it.