# PhoneOperatorChecker

### Description

This web service provides mobile phone operator and region for given phone number (only for country code +7)

### Programming stack:

- Frontend: Vue3, Vuetify, Axios
- Backend: Flask, Dependency Injector, Gunicorn, PostgreSQL
- DevOps: Docker, Docker Compose, NginX (as reverse-proxy)

### Start Up

1. Install required software: Docker, Docker Compose
2. Unzip the archive *./db/data.zip* into *./db/data*
    - Optional: if you **don't want** PostgreSQL container to create its volume in ./db/postgres-data then comment  
      `./db/postgres-data:/var/lib/postgresql/data` in *./docker-compose.yaml*
3. Run containers by...
    - executing *./run.sh*
    - or manually: `docker-compose pull; docker-compose up --build -d`
4. Open your browser at [http://localhost:8001](http://localhost:8001)
    - Note: first start-up of the database container might be quite long
5. Enjoy